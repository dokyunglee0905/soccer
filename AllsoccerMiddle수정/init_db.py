from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dballsoccer

epl = [
    {'team_id':1, 'name': '토트넘', 'img_url': 'https://4.bp.blogspot.com/-ky4K3JuN80I/VlAzAA000SI/AAAAAAAACFc/QbVkjNwcqQ0/w1200-h630-p-k-no-nu/Tottenham%2BHotspur.png', 'like': 0, 'status': '토트넘', 'league':'EPL'}
]

laliga = [
    {'team_id':21, 'name': '레알 마드리드 CF', 'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FGQehl%2FbtqEghIQCXV%2Fsgicu1CAbXG90YZal02zr1%2Fimg.png', 'like': 0, 'status': '레알 마드리드', 'league':'La Liga'}
]

bundesliga = [
    {'team_id':41, 'name': 'FC 바이에른 뮌헨', 'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkGDcN%2FbtqEmo9yRjd%2FeMTxROqp7EaAymuK6DdNz0%2Fimg.png', 'like': 0, 'status': '바이에르 뮌헨', 'league':'Bundesliga'}
]

db.team.drop()
db.team.insert_many(epl)
db.team.insert_many(laliga)
db.team.insert_many(bundesliga)

