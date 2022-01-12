from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
client = MongoClient('localhost', 27017)
db = client.dballsoccer

epl = [
    {'team_id':1, 'name': '토트넘', 'img_url': 'https://4.bp.blogspot.com/-ky4K3JuN80I/VlAzAA000SI/AAAAAAAACFc/QbVkjNwcqQ0/w1200-h630-p-k-no-nu/Tottenham%2BHotspur.png', 'like': 0, 'status': '토트넘', 'league':'EPL'}
]

laliga = [
    {'team_id':21, 'name': '레알 마드리드 CF', 'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FGQehl%2FbtqEghIQCXV%2Fsgicu1CAbXG90YZal02zr1%2Fimg.png', 'like': 0, 'status': '레알 마드리드', 'league':'La Liga'}
]

bundesliga = [
    {'team_id':41, 'name': 'FC 바이에른 뮌헨', 'img_url': 'https://w.namu.la/s/69ba3ae15fc080623ef6f64e7232bdd5a82fc2847585653dd5342f51eb61f8ffe802b29c93c49d5f2afedf05e7a89dd15d84faa1e58f7bb7af602014b278f056a48d46cddf984a5db06d54e47bb499e3060a72ff9644f95c5e2c9ab8ec393e1c', 'like': 0, 'status': '독일 분데스리가의 대표 프로 축구 클럽. 연고지는 독일 바이에른 자유주 뮌헨. 홈 경기장은 알리안츠 아레나이다.', 'league':'Bundesliga'},
    {'team_id':42, 'name': '도르트문트', 'img_url': 'https://w.namu.la/s/a2abee3349efc3427d7789c56e00dc43f0e6970188e06c6b55b56978dfed36ebade3f54a9593bfd1671998795575396d36ea2fa026cdb4732a8260c6aef3418af869e46d76953d40110ccbbccde3f59d2c0c7c6132e153f23fbf17196fac5a8d', 'like': 0, 'status': 'FC 바이에른 뮌헨과 더불어 분데스리가를 양분하고 있는 독일의 빅클럽이다.홈 구장은 지그날 이두나 파크', 'league':'Bundesliga'},
    {'team_id':43, 'name': '레버쿠젠', 'img_url': 'https://w.namu.la/s/018e0eca6c590a2fa4ad3bf9ff7aab08af88c03b953eb780200b2413805c003943428e3cb8fe72a9688c00f61d7331772a2a197ad01583cd8fc6be953760fe6c2ab03d4ce07805e012332eebbac3d6389ddd5294a9f35e1321c9d344eeb95c2a', 'like': 0, 'status': 'TSV 바이어 04 레버쿠젠은 독일 노르트라인베스트팔렌 주 쾰른 현 레버쿠젠을 연고로 하는 종합 스포츠 클럽이다.', 'league':'Bundesliga'},
    {'team_id':44, 'name': '호펜하임', 'img_url': 'https://w.namu.la/s/2a5e714cd55b73cb371fd6a4a03d24a03d41dcba2f44a008bc6aa6fd1d65f10db047b5a7bdaec106aa8a678dca7d4c18513f23281e8c4125f3c608361169891a8992381e273bc5409b870b53fc17ccca05a7090ec9bed9a59ed8fa83d2fc2e0f', 'like': 0, 'status': '독일 분데스리가 소속 프로축구단. 바덴뷔르템베르크 주 진스하임 시의 외곽에 있는 호펜하임 지역을 연고지로 삼고 있다', 'league':'Bundesliga'},
    {'team_id':45, 'name': '프라이부르크', 'img_url': 'https://w.namu.la/s/f0ccf9214af3fea62e874df9ce221a4df08554bcf6325f0f68ae7faf9e39d5603f6ed5455dee8fc1fc3c690be53cb76c1babf5d467bc4c9660fde247b9c088faf3863bb3f4f27fd317477ddb3d07c502516406373a61ac7b35b643ac1239253d', 'like': 0, 'status': '독일 분데스리가의 축구클럽. 태양의 도시라는 별칭으로 유명한 프라이부르크를 연고로 한 팀이다.', 'league':'Bundesliga'},
    {'team_id':46, 'name': '쾰른', 'img_url': 'https://w.namu.la/s/5a19595dd8c366eff0c49a313fc4a46c8fcdaca60b0acb57113eff85f66bd7d3544f272c3769ee47fef95b06a2414ed5697ca2e39ea45e4f0e08b89c7e4692e8b5ad69c797d269bf7f0595e42b2097c5c4e7f071d04f21a1fdf63c9352fa5360', 'like': 0, 'status': '독일 분데스리가의 축구클럽.여러 스포츠팀을 보유한 클럽이지만 보통 축구클럽으로 더 알려져 있다. 분데스리가의 초대 챔피언이기도 하다.', 'league':'Bundesliga'},
    {'team_id':47, 'name': '우니온 베를린', 'img_url': 'https://w.namu.la/s/aba72c358dce134126596e29d4d8173708d9a1953ae6e145b803278a15b92212e7f8a48fab0ae7acf84cb8708819c3def9127ef8b67a20666ab4ddb33db6cf7df9a5649d838a8119178dfba4b03f3a23bd6747d9fe52c267150eb14566915d52', 'like': 0, 'status': '.FC 우니온 베를린은 베를린을 연고로 하는 독일의 프로축구 클럽이다.', 'league':'Bundesliga'},
    {'team_id':48, 'name': '프랑크푸르트', 'img_url': 'https://w.namu.la/s/42ef3069672ab4060c0c1ac367242781048e7acdb7cb7840cfc7c04aec8dd02391c997ccf2c70466ee71a3045cb7df7cb64cca1fbc02c137a87becb36d852ae2838f8bd58669d44aa9d25d0afd48ed1140edfb387395cb8d957080403daacdd926bc676b388cb3d5dfed1c13e73722f1', 'like': 0, 'status': 'FC 프랑크푸르트는 독일 브란덴부르크 주 프랑크푸르트안데어오더를 연고로 하는 축구 클럽이다. 헤센 주의 아인트라흐트 프랑크푸르트와는 연고지부터 다른 구단이다.', 'league':'Bundesliga'},
    {'team_id':49, 'name': '라이프치히', 'img_url': 'https://w.namu.la/s/3ecc0d2ff166c284cb467eec18276d79a527fef52f63f8737fae98196a20314b32df54ba1697e8df73fe3a985678d1886f18f54547d9c7ef16becbb1cd57b40903e2d5b5e3d24a6b4e8b2c80410ca36c23a5a0f00125b00464470602a341bef7', 'like': 0, 'status': '독일 작센 주의 라이프치히를 연고로 하는 축구 클럽 2018-19 시즌까지만 해도 분데스리가 팀에서 유일하게 구 서독 지역이 아닌 구 동독 지역에 속해있던 팀이다. ', 'league':'Bundesliga'},
    {'team_id':50, 'name': '마인츠', 'img_url': 'https://w.namu.la/s/e35111b06df9c560de0b65d6c11dad80f2678e01dace5d88084a0ef68ccec4fd30ff6bf58181e8775e7962ef9ccd905fa0441b02846a0e8c003944dc1a4649272e137b35a8698b21ef5ab4df5fe3ba83bffa9ac8b29bd078bfeeffb5aab40798', 'like': 0, 'status': '독일 라인란트팔츠 주 마인츠를 연고로 하는 축구구단. 현재 분데스리가에 소속되어 있다.', 'league':'Bundesliga'},
    {'team_id':51, 'name': '보훔', 'img_url': 'https://w.namu.la/s/e566c3d9a60ed76c2bc814a3305ca53b4d97d387dd438eb33fc893cd37d0b98cf588b39c77b87c31caa9732cf98909519fe83fd7beb13dcaf35e1d6e621ef5b0af84594f26d5fade438083d02209bd102f44272c6c46b14e3515b18a0ea67dc4', 'like': 0, 'status': '독일 분데스리가의 축구 클럽. 1848년에 창립된, 세계에서 가장 오래된 축구 구단이다.', 'league':'Bundesliga'},
    {'team_id':52, 'name': '뮌헨글라트바흐', 'img_url': 'https://w.namu.la/s/0f561c48725cef5f738f0a709c8c7aa76cb4c08d0eff532e9da0d877fc7cd3c445db21ca05c04816e57b8cd04063cb89ab6e75fafca916064a62b98cd9b243a92994deb506d033504c6d3ce5b75a85a1506b229a664290b5020f41eac8f3bb7b', 'like': 0, 'status': '독일의 프로 축구팀. 최상위리그인 분데스리가에 소속되어 있다. 연고지는 독일의 대표적인 군수산업 도시인 노르트라인베스트팔렌 주 묀헨글라트바흐 시이며, 경기장은 보루시아 파르크이다. ', 'league':'Bundesliga'},
    {'team_id':53, 'name': '헤르타BSC', 'img_url': 'https://w.namu.la/s/23882540be35d8a4ddc3d45b47ae187975211c98b99fe4e0fa04047295d42491e88386d359111c34bb12eec05bcd980e8faba844bbfea22abaec62962edfcb25d2b41c48d5627a60e2936a628119b0652bc2cd41fd06003669a0000918886dea', 'like': 0, 'status': '헤르타 BSC는 독일의 수도 베를린을 연고로 하는 스포츠 클럽이다.', 'league':'Bundesliga'},
    {'team_id':54, 'name': '볼프스부르크', 'img_url': 'https://w.namu.la/s/9a6e533d775170265531a172a63a1693f888e751639d18485dffe2237c574440f764ac73a3a32097e3bce3347b13dc7f29cfaaa9a100f630c0364fd33bbb1a7dfbe99e860f0611570e7f670954ca0d7f9ac0468ba62ba5cdab14eee50f5f891e', 'like': 0, 'status': '독일 분데스리가의 축구 클럽. 신흥강호 축에 속하는 이 팀의 역사는 폭스바겐과 떼어놓고 말할 수 없다.', 'league':'Bundesliga'},
    {'team_id':55, 'name': '슈투트가르트', 'img_url': 'https://w.namu.la/s/5a48833f1c019b62be6aa5ae7e708961dc58ab9a70f10c052f8b27b5f3d3fead406ee184e3700a61f5b8d689f8a709c48f6f3001ac7b1bf394545f7f7e2bc8cee70a5d537db1aabd6eaa5905c1d20937021c5e9d1cc0ec03c84b63119ec91241a8e17a1b43e88b5a8769ed09f0ebce0c', 'like': 0, 'status': '독일 분데스리가의 축구 클럽. 종합 스포츠 클럽으로 피스트볼, 탁구, 하키 등을 운영하는데 그 중 유명한 것이 바로 축구 클럽이다. 남독일의 주요 도시 중 하나인 슈투트가르트를 연고로 4만5천명의 회원을 자랑하는 독일에서 다섯번째로 큰 클럽이다.', 'league':'Bundesliga'},
    {'team_id':56, 'name': '아우크스부르크', 'img_url': 'https://w.namu.la/s/c353f03ca4fe2078ac9c3ddc056d87d5c1aeaa5323c56c02352143c39b0a9f7ab85268b9c5341264935cde6f7499ef31419f7bb5459534e28c772d0c986efac78dcc91e9345ae587ed64deffa08d882b56ea6f0328b500bc317c52c8f2123be1', 'like': 0, 'status': '독일 분데스리가의 축구 클럽. 구자철, 홍정호, 지동원이 뛰며 한국에 이름을 알렸다.', 'league':'Bundesliga'},
    {'team_id':57, 'name': '빌레펠트', 'img_url': 'https://w.namu.la/s/3dbbace203b6eca41a04a7bffd3dcf3322f08ec942fce6b93072da849346149737de8509b07fd09a7cb2252aabd49abf54bf7d14578ded9691c55a3598ff0a74cda9729211ef3281e1a9db7bb5d327143c407bc3d1ef1aa788094b47936672d0', 'like': 0, 'status': 'DSC 아르미니아 빌레펠트는 독일 노르트라인베스트팔렌 주 빌레펠트의 축구 클럽 팀이다.', 'league':'Bundesliga'},
    {'team_id':58, 'name': '퓌르트', 'img_url': 'https://w.namu.la/s/c2b52a73899d75c8d2b6f5141898d09a11cbf96f0db65d24ae9657755c7a2df4ee0b0872d8a687d9e5b616283d3db9f83bb8ade60531138cda89fd0f1404dbeb3946f16f3dec080c2264b68cf85fca6c896e3ca38a11799e0b4b9edfe7e1b538', 'like': 0, 'status': 'SpVgg 그로이터 퓌르트는 독일 바이에른 주 퓌르트의 축구 클럽 팀이다. 제2차 세계 대전 전에 3번의 우승을 차지하였다.', 'league':'Bundesliga'}
]

db.team.drop()
db.team.insert_many(epl)
db.team.insert_many(laliga)
db.team.insert_many(bundesliga)

# 순위
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/wfootball/index.nhn',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

epl = soup.select('#_team_rank_epl > table > tbody > tr')
bundesliga = soup.select('#_team_rank_bundesliga > table > tbody > tr')
primera = soup.select('#_team_rank_primera > table > tbody > tr')

db.eplrank.drop()

for tr in epl:
    league = 'EPL'
    teamrank = tr.select_one('th > span > em').text.strip()
    teamname = tr.select_one('td:nth-child(2) > div > div.info > span').text.strip()
    round= tr.select_one('td:nth-child(3) > span').text.strip()
    win = tr.select_one('td:nth-child(4) > span').text.strip()
    tie = tr.select_one('td:nth-child(5) > span').text.strip()
    lose = tr.select_one('td:nth-child(6) > span').text.strip()
    pts = tr.select_one('td:nth-child(7) > span').text.strip()

    doc = {
        'league' : league,
        'teamrank' : teamrank,
        'teamname' : teamname,
        'round' : round,
        'win' : win,
        'tie' : tie,
        'lose' : lose,
        'pts' : pts
    }

    db.eplrank.insert_one(doc)

for tr in primera:
    league = 'La Liga'
    teamrank = tr.select_one('th > span > em').text.strip()
    teamname = tr.select_one('td:nth-child(2) > div > div.info > span').text.strip()
    round= tr.select_one('td:nth-child(3) > span').text.strip()
    win = tr.select_one('td:nth-child(4) > span').text.strip()
    tie = tr.select_one('td:nth-child(5) > span').text.strip()
    lose = tr.select_one('td:nth-child(6) > span').text.strip()
    pts = tr.select_one('td:nth-child(7) > span').text.strip()

    doc = {
        'league' : league,
        'teamrank' : teamrank,
        'teamname' : teamname,
        'round' : round,
        'win' : win,
        'tie' : tie,
        'lose' : lose,
        'pts' : pts
    }

    db.eplrank.insert_one(doc)

for tr in bundesliga:
    league = 'Bundesliga'
    teamrank = tr.select_one('th > span > em').text.strip()
    teamname = tr.select_one('td:nth-child(2) > div > div.info > span').text.strip()
    round= tr.select_one('td:nth-child(3) > span').text.strip()
    win = tr.select_one('td:nth-child(4) > span').text.strip()
    tie = tr.select_one('td:nth-child(5) > span').text.strip()
    lose = tr.select_one('td:nth-child(6) > span').text.strip()
    pts = tr.select_one('td:nth-child(7) > span').text.strip()

    doc = {
        'league' : league,
        'teamrank' : teamrank,
        'teamname' : teamname,
        'round' : round,
        'win' : win,
        'tie' : tie,
        'lose' : lose,
        'pts' : pts
    }

    db.eplrank.insert_one(doc)
