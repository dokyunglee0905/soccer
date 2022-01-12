from pymongo import MongoClient
import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'ALLSOCCER'

client = MongoClient('localhost', 27017)
db = client.dballsoccer


@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    # JWT 디코드하여 paylod에 정보 저장
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 로그인 정보로 사용자의 아이디를 가져옴
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('index.html', user_info=user_info['username'])
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,  # 아이디
        "password": password_hash,  # 비밀번호
        "profile_name": username_receive,  # 프로필 이름 기본값은 아이디
        "profile_pic": "",  # 프로필 사진 파일 이름
        "profile_pic_real": "profile_pics/profile_placeholder.png",  # 프로필 사진 기본 이미지
        "profile_info": ""  # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


# 로그인 후, 축구 조회 API
@app.route('/mainpage', methods=['GET'])
def soccerTeam_list():
    # 어떤 축구의 팀을 가져올지 'league'이란 변수명에 담겨진 값을 가져와 비교
    target = request.args.get('league');

    # 만일 리그가 없는. 즉 모든 리그의 팀을 가져오라는 이벤트일 경우 모두 가져오고 그렇지 않을경우 리그 조회하여 가져온다.
    if target is not None:
        soccerTeam = list(db.team.find({'league': target}, {'_id': False}).sort('like', -1))
    else:
        soccerTeam = list(db.team.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'result': 'success', 'all_Teams': soccerTeam})


# 좋아요
@app.route('/like', methods=['POST'])
def teams_like():
    # 이벤트가 발생한 팀 이름으로 조회하여 해당 팀 좋아요 갯수를 1 증가시킨다.
    name_receive = request.form['name_give']
    like = db.team.find_one({'name': name_receive})
    new_like = like['like'] + 1

    db.team.update_one({'name': name_receive}, {'$set': {'like': new_like}})
    return jsonify({'result': 'success'})


# 리뷰 불러오기
@app.route('/get_comment', methods=['GET'])
def comment_list():
    # 해당하는 팀 고유아이디와 고유 코멘트를 가져온다.
    teamid = request.args.get('teamComment')
    comments = list(db.review.find({'team_id': teamid}))
    for comment in comments:
        comment["_id"] = str(comment["_id"])
    return jsonify({'result': 'success', 'commentList': comments})


# 리뷰작성
@app.route('/comment', methods=['POST'])
def teams_review():
    try:
        # 입력받은 코멘트와, 사용자의 아이디 그리고 해당되는 팀 아이디를 배열에 저장하고 해당 배열을 데이터 베이스에 입력한다.
        comment_receive = request.form['comment_give']
        teamId = request.form['teamId']
        username = request.form['username']
        doc = {
            'team_id': teamId,
            'username': username,
            'comment': comment_receive,
        }
        db.review.insert_one(doc)
        return jsonify({'result': 'success'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


# 리뷰 삭제
@app.route('/comment_delete', methods=['POST'])
def review_delete():
    # 해당 리뷰를 작성한 작성자일 경우, 코멘트의 고유아이디값을 조회해 해당 이벤트가 일어난 코멘트값만 삭제한다.
    comment_receive = request.form['comment_give']
    db.review.delete_one({'_id': ObjectId(comment_receive)})
    return jsonify({'result': 'success'})


# 순위
@app.route('/rank/list', methods=['GET'])
def show_rank():
    # 어떤 축구의 팀을 가져올지 'league'이란 변수명에 담겨진 값을 가져와 비교
    target = request.args.get('league');

    # 만일 리그가 없는. 즉 모든 리그의 팀을 가져오라는 이벤트일 경우 모두 가져오고 그렇지 않을경우 리그 조회하여 가져온다.
    if target is not None:
        team_rank = list(db.eplrank.find({'league': target}, {'_id': False}).sort('pts', -1))
    else:
        team_rank = ''
    return jsonify({'result': 'success', 'all_ranks': team_rank})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
