from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
client = MongoClient('localhost', 27017)
db = client.dballsoccer

epl = [
    {'team_id': 1, 'name': '토트넘 홋스퍼 FC',
     'img_url': 'https://post-phinf.pstatic.net/MjAxOTAyMTNfMTg5/MDAxNTUwMDQ1NTc0Mzk1.hhJukdYzsSmvfuX4FSXgOkOxSXrqddJtVxhlFFYsSW0g.WZ6nyu_Bta2EqoMHxyWfgklMYL5kYCYpU0CFyS-9mxog.PNG/spurs-blue-no-text-300x300.png?type=w1200',
     'like': 0, 'status': '영국 클럽 최초의 유럽 대항전 우승, UEFA 유로파 리그 초대 우승 클럽. 애칭은 스퍼스(Spurs).', 'league': 'EPL'},
    {'team_id': 2, 'name': '첼시 FC',
     'img_url': 'https://upload.wikimedia.org/wikipedia/ko/thumb/a/ae/Chelsea_FC_Logo.svg/1200px-Chelsea_FC_Logo.svg.png',
     'like': 0, 'status': '영국 클럽 최초로 UEFA 3대 메이저 대회를 모두 제패한 런던 최고의 빅클럽이자 잉글랜드의 명문 클럽. ',
     'league': 'EPL'},
    {'team_id': 3, 'name': '맨체스터 유나이티드 FC',
     'img_url': 'http://pngimg.com/uploads/manchester_united/manchester_united_PNG27.png', 'like': 0, 'status': '영국 잉글랜드 그레이터맨체스터 주의 트래포드를 연고로 하는 프로 축구 클럽. 뉴턴 히스 LYR F.C.(Newton Heath LYR F.C.)란 이름으로 창설되었다.',
     'league': 'EPL'},
    {'team_id': 4, 'name': '아스널 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/dfdza0/btqD9u4yxr2/zMiJQjhtw8dvWfpltl0u3k/img.png', 'like': 0,
     'status': '잉글랜드 1부리그 통산 13회 우승으로 잉글랜드 전체 클럽 중 3위에 위치하고 있으며, 특히 프리미어 리그 출범 이후 유일한 무패 우승과 FA컵 역대 최다 우승 등의 기록을 보유하고 있는 잉글랜드 명문 클럽이기도 하다.',
     'league': 'EPL'},
    {'team_id': 5, 'name': '맨체스터 시티 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/6nlSa/btqEam5EQkN/YR2cYwIP7WshkKAcQq3GLK/img.png', 'like': 0,
     'status': '만수르 자본의 유입 후 2010년대 화려한 전성기를 구사했고 여전히 막강한 위력을 뽐내며 이젠 구단의 최종 목표에 도전하는 유럽에서 손에 꼽히는 강팀이자 빅클럽이 되었다.',
     'league': 'EPL'},
    {'team_id': 6, 'name': '리버풀 FC',
     'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FclN818%2FbtqEbaXWlmI%2FyDNYr7RUtrTl7EaSiNTsT0%2Fimg.png',
     'like': 0,
     'status': '잉글랜드 클럽 중 UEFA 챔피언스 리그 최다 우승팀으로 잉글랜드에서 유일하게 빅 이어를 영구 소장한 명문 클럽이다.',
     'league': 'EPL'},
    {'team_id': 7, 'name': '레스터 시티 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/cjYGPR/btqEcnI26hP/QSG7VlwltLiSgDTJsDKBM1/img.png', 'like': 0,
     'status': '인구 30만(광역 도시권 80만)의 도시 레스터를 대표하는 축구 클럽이다. 단 한 시즌간 3부 리그 생활을 한 것을 제외하고 모든 역사를 1~2부 리그에서만 보낸, 나름의 역사를 지닌 클럽이다.',
     'league': 'EPL'},
    {'team_id': 8, 'name': '웨스트햄 유나이티드 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/oQOj5/btqEcU9btKB/plaaFAULI1QLX0AUqKWwH1/img.png', 'like': 0,
     'status': '잉글랜드 프리미어리그 소속 축구 클럽. 정식명칭은 웨스트햄 유나이티드 축구 클럽(West Ham United Football Club)으로 1895년 조선소 노동자들에 의해서 창단되었다.',
     'league': 'EPL'},
    {'team_id': 9, 'name': '울버햄튼 원더러스 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/cCQxgR/btqEanw8W9C/0crbbRJ9Rcdk11UPRtqTBK/img.png', 'like': 0,
     'status': '잉글랜드의 울버햄프턴을 연고로 하는 축구 클럽이다. 1877년 교회의 존 베인튼과 존 브로디라는 두 신부가 세인트 루크스라는 이름으로 창단하였고, 2년 뒤 더 원더러스와 합병하여 지금의 울버햄튼 원더러스 FC라는 이름을 가지게 되었다.',
     'league': 'EPL'},
    {'team_id': 10, 'name': '브라이튼 앤 호브 알비온 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/GyBKz/btqEbtSfbBN/1y3Sg38N7yb9kITbElwua1/img.png', 'like': 0,
     'status': '영국 잉글랜드 남동부 이스트서식스 주 브라이튼앤호브 보로에 연고지를 둔 축구 클럽, 브라이튼시의 북동쪽에 자리잡고 있다.',
     'league': 'EPL'},
    {'team_id': 11, 'name': '사우샘프턴 FC',
     'img_url': 'http://assets.stickpng.com/images/580b57fcd9996e24bc43c4ea.png', 'like': 0,
     'status': '잉글랜드의 프로 축구 클럽으로 1885년 "성공회 세인트 메리 성당 청년회(St. Marys Church of England Young Mens Association)"라는 이름으로 설립된 구단으로 2021-22 시즌 현재 잉글리시 프리미어 리그를 구성하는 20개 구단 중 하나이다.',
     'league': 'EPL'},
    {'team_id': 12, 'name': '크리스탈 팰리스 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/bKkfDf/btqEep7VPx5/XKGVK2LkfpThRDkXOGt891/img.png', 'like': 0,
     'status': '1905년 영국 런던의 남부 지역을 연고로 창단한 축구 클럽. 인근에 있었던 런던의 건축물 크리스탈 팰리스(Crystal Palace, 수정궁)에서 이름을 따서 만들어졌고, 이 때문에 대한민국의 축구 팬들도 흔히 수정궁이라고 애칭 삼아 부른다.',
     'league': 'EPL'},
    {'team_id': 13, 'name': '뉴캐슬 유나이티드 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/cgRzLZ/btqEd8FDGhL/3Lj0yoBQL07z8JVgk033dk/img.png', 'like': 0,
     'status': '잉글랜드 역대 최고의 명장과 스트라이커로 꼽히는 바비 롭슨 경과 앨런 시어러가 몸담았던 명문 클럽이다. 현재는 20개 팀 중에 19위를 차지하는 최하위권 팀이다.',
     'league': 'EPL'},
    {'team_id': 14, 'name': '브렌트포드 FC',
     'img_url': 'https://www.pngmart.com/files/10/Brentford-PNG-File.png', 'like': 0,
     'status': '프리미어 리그 소속 잉글랜드 런던 서부 브렌트포드에 위치한 축구단. 런던을 연고지로 하는 수많은 프로축구팀 중에서도 내세울 만한 역사를 딱히 가지지 못한 상대적 약소 팀이었다. 그러나 2020-21 시즌 플레이오프를 거친 후 74년 만에 1부 리그 입성에 성공했다.',
     'league': 'EPL'},
    {'team_id': 15, 'name': '아스톤 빌라 FC',
     'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FFqkbV%2FbtqEcmkPDZn%2FkKWnIgKvUjL7DNaj5Fnj51%2Fimg.png',
     'like': 0,
     'status': '잉글랜드 프로축구의 역사와 함께 해온 오랜 전통을 자랑하는 클럽. 워낙 전통적인 강팀으로 유명하다보니 현지에서도 팬들의 자부심이 정말 대단하고 다른 팬들도 많이 알아주는 편이다.',
     'league': 'EPL'},
    {'team_id': 16, 'name': '에버턴 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/wpECa/btqEbRyfZS7/gKgnlwHWb229zF8yW4wLa1/img.png', 'like': 0,
     'status': '에버튼 FC는 1878년에 창단된 잉글랜드 리버풀 시를 연고로 하는 프리미어 리그의 축구 클럽이다. 에버튼은 2020-21 시즌 기준으로, 잉글랜드의 최상위 축구 리그에 가장 많이 참여하고 있는 팀이다',
     'league': 'EPL'},
    {'team_id': 17, 'name': '리즈 유나이티드 FC',
     'img_url': 'https://t2.daumcdn.net/thumb/R720x0.fpng/?fname=http://t1.daumcdn.net/brunch/service/user/akJj/image/q6kk5iskR2B6YJnqAtG0mGbEX-M.png',
     'like': 0,
     'status': '잉글랜드의 프로축구단.요크셔험버 웨스트요크셔 주 리즈를 연고지로 하고 있다. 맨체스터 유나이티드 FC와 로즈 더비를 가졌을 정도로 프리미어 리그에 오래 있었지만 2003-04 시즌을 끝으로 강등된 후 2019-20 시즌까지 EFL 챔피언십에 있었다.',
     'league': 'EPL'},
    {'team_id': 18, 'name': '왓포드 FC',
     'img_url': 'https://blog.kakaocdn.net/dn/niqMJ/btqEepHbIgj/FDJvIPWBeFOyChSUXPAJKk/img.png', 'like': 0,
     'status': '왓포드 축구 클럽(Watford Football Club)은 런던 서북쪽의 위성도시 하트퍼드셔 주 왓포드를 연고로 하는 영국 잉글랜드의 프로 축구 클럽이다.',
     'league': 'EPL'},
    {'team_id': 19, 'name': '번리 FC',
     'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkLyDh%2FbtqEbQkPaxf%2FG1EKJtCl1ON87sQbxlW6HK%2Fimg.png',
     'like': 0,
     'status': '번리 FC(Burnley Football Club)는 잉글랜드 번리에 연고지를 둔 축구 클럽으로 1882년 창단하였다. 풋볼 리그의 원년부터 참여한 유서깊은 구단으로, 클럽의 컬러는 레드와인과 블루를 사용하는데, 풋볼 리그 출범 초기의 최강팀이었던 아스톤 빌라의 강함을 본받고 싶어 컬러를 변경한 것이다.',
     'league': 'EPL'},
    {'team_id': 20, 'name': '노리치 시티 FC',
     'img_url': 'https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fco5k34%2FbtqEdkfzg7C%2Fjd05vdzW1HMdjS8GaLi5t0%2Fimg.png',
     'like': 0,
     'status': '홈에서 골을 넣었을 때 경기장에 울려퍼지는 "쌈바~"가 인상깊은 클럽. 노란 홈 유니폼과 "카나리아들"이란 별명 등 왠지 브라질스럽다.',
     'league': 'EPL'}
]

laliga = [
    {'team_id':21, 'name': '레알 마드리드 CF', 'img_url': 'https://w.namu.la/s/3600bcececc818b7cac00f560e077ef277caece0abc70b13a1194c0333de4763b0a4a6e44eea387f6108992836bf73955983199e702100ff91b422acf80e28f1e5df4bee631f84153e59b232737268eca8fbc5c3472d990f6a4fd184bc7bcffb', 'like': 0, 'status': 'UEFA 챔피언스 리그, 라리가 양대 최다 우승을 자랑하는 구단으로, 1928년 라리가가 창설된 이후 단 한 번도 1부 리그에서 강등당하지 않았다. 20세기부터 현재까지 세계에서 가장 성공적인 축구 클럽이며, 자국 라이벌 FC 바르셀로나와 함께 라리가를 양분하고 있고 범위를 전 세계로 넓혀도 최고의 명문 축구 클럽으로 첫 손에 꼽힌다.', 'league':'La Liga'},
    {'team_id':22, 'name': '바르셀로나', 'img_url': 'https://w.namu.la/s/f83da2c487a63641735b179f727d6b4ef81895745171c28881be65aeb5c83a1cd2fb5a7a8b51d26a0dc73ab8f8be4265d21184931f279019acd5a1bad355159ae843656f6f8f9d9b98e857f324a67d58994684a2566bbcbe75c8c6f51862ff84', 'like': 0, 'status': '스페인 라리가의 프로 축구 클럽. 연고지는 바르셀로나. 홈 구장은 캄 노우. 유럽 축구 역사상 최초로 6관왕과 2회의 트레블을 달성한 명문 구단이다. 라리가 초대 우승을 차지한 이래 라이벌 레알 마드리드 CF에 이어 2번째로 많은 라리가 우승을 기록했고, 1928년 라리가 출범 이래 단 한 번도 강등되지 않고 스페인 최상위 리그에서 뛰고 있다.', 'league':'La Liga'},
    {'team_id':23, 'name': 'AT마드리드', 'img_url': 'https://w.namu.la/s/21062b547855d10c500ab1092dbcf0148f5f94b6a30f9477249582189092616ee2c26b5770bd959bc962da09a0c55f5b35677804a6e099e162ae69cd27f3867778149d487f74b50bf1758eff0b1a1e4f23c3b624faf48d012f9e42774568e391', 'like': 0, 'status': '스페인 라리가의 프로 축구 클럽. 연고지는 마드리드. 홈 구장은 완다 메트로폴리타노이다. 2010년대에 이르러서 클럽의 비약적인 발전으로 많은 사람들이 신흥 강호로 알고 있지만 역사적으로 꾸준히 라리가와 유럽 대항전에서 많은 활약을 해온 강팀이다', 'league':'La Liga'},
    {'team_id':24, 'name': '발렌시아', 'img_url': 'https://w.namu.la/s/81592ee6b1440e7753f493d8f8cce254aee2596389030a3ae767182faed685cc3c33eb44e400edda06ed1a39f29d269d127dfe3858da3b3959b26afadfb161f044929b17e0ce55a5102c1a57d36e93684a9ef418657df4b13048f7bd7577be16', 'like': 0, 'status': '스페인 라리가 소속의 팀으로 최근 수년간의 암흑기를 지나 다시 한 번 반등을 꿈꾸는 스페인 전통의 명문 클럽이다. 홈구장은 49,800명을 수용할 수 있는 메스타야이며 별칭은 박쥐군단.', 'league':'La Liga'},
    {'team_id':25, 'name': '비야레알', 'img_url': 'https://w.namu.la/s/63afad938f588bed1a8e9c2e1b387bce501cf08a5252b4e673d2431db53e1f7e996556025b353ecc94164872cda3563405b3f412efb5960b2fe9ca4e6d5144712fca664473497c83bb81e15cb74fb49bd55dd0727e1525faeb4c9173d38d331e', 'like': 0, 'status': '비야레알 클럽 데 풋볼은 스페인 프로축구리그에 소속된 클럽으로, 1923년 창단됐다. 연고지는 카스테욘 주 비야레알이다. 홈구장은 23,500명을 수용할 수 있는 에스타디오 데 라 세라미카다. 흔히 비야레알 CF나 비야레알로 불리며, 노란 잠수함이라는 별명으로도 널리 알려져 있다.', 'league':'La Liga'},
    {'team_id':26, 'name': '바예카노', 'img_url': 'https://w.namu.la/s/ea6140098451926a8b266b587be160c86be6b29570cfe59e4d2d621ca15d5b12863ae5c4616ca1afe3a9b541a7a723e31f89631e3315bc09614738c1edb356382f701ded98cf2ba37abeaf313e313365927121025c9924376179d758c512c906', 'like': 0, 'status': '스페인 수도 마드리드를 연고로 하고 있는 중소클럽이다. 마드리드 외곽 바예카스 마을의 노동자들에 의해 1924년에 창설됐다.', 'league':'La Liga'},
    {'team_id':27, 'name': '레알 소시에다드', 'img_url': 'https://w.namu.la/s/6d7bb53be3a8a3f8e0200a7cf8b8b01ef2615b801e29eec396b73fb40f5ae75a2fbdde37fd7877e0d792b2c7966ab8318a94e65f421547f46aa09e6aa67b6530f6cc38539f453030faef3cf722f4b1cdd49f88eb87a43dbcf5df92fe4a7b881f', 'like': 0, 'status': '스페인의 프로축구단으로, 아틀레틱 빌바오와 함께 스페인 바스크 지방을 대표하는 클럽이다. 아틀레틱 빌바오와 전통의 라이벌이자 이웃사촌에 가까운 관계이며, 두 팀의 경기는 바스크 더비라는 이름으로 불린다.', 'league':'La Liga'},
    {'team_id':28, 'name': '아틀레틱', 'img_url': 'https://w.namu.la/s/96b9e92e018bfa13ddc423cd38e456fbabca0cd798e2165a87cbc3108444d016bc7cb688e89ffc5094c31c9cc1fbcf2b186061fe9278db49fc653f9a4fc5fc94d5813d455d1f8399db31052b2c3fd8309d9aa43b08513f145630d5065431a70c', 'like': 0, 'status': '스페인의 바스크 지방을 대표하는 프로 축구 클럽. 팀의 라리가 최초 우승이 라리가 최초의 무패우승(1929-30 시즌)이라는 대기록과 레알 마드리드와 FC 바르셀로나, 아틀레티코 마드리드에 이어 4번째로 많은 31회(리그 8회, 국왕컵 23회)의 트로피를 들어올린 기록을 가진 스페인의 명문 클럽이다.', 'league':'La Liga'},
    {'team_id':29, 'name': '에스파뇰', 'img_url': 'https://w.namu.la/s/9277ac2b0a49f4aad5be79149094f4166672cdbc4c554b288e64fa2217517e4c3a6e9799776c5d18cb97cf39183b63c46e47cd2c7408d1c56a8773d81cd4a034c4e76bbb3894d9b9275948327872dd0afb8f9dc76cf383672754aa4ace7d0d77', 'like': 0, 'status': '스페인의 라리가 소속 프로축구클럽이다. 1900년 카탈루냐의 중심도시 바르셀로나에 카스티야인들을 위해 만들어진 구단이다. ', 'league':'La Liga'},
    {'team_id':30, 'name': '세비야', 'img_url': 'https://w.namu.la/s/feaaf4aba3d476a21b040d45a9ae861c1607c7d4552bd84dbb9a913c3130635aa821fe979a0dd980ac0968baa4db8811bbc484f8aeeba5a1ced5f7a58a3241ef3b36dfc38719a6d04a35a14d44b90223d2ff51ec9c773383497a8663bd6793c9e1ce00777d3d50af210d85c96c30aad9', 'like': 0, 'status': '100년 이상의 오랜 전통을 자랑하는, 세비야 동부 특유의 자부심을 상징하는 클럽. 레알 베티스와 오랫동안 스페인 남부 안달루시아 지방의 맹주 자리를 놓고 다투어 온 것으로 유명하다. 라리가 우승은 1회(1945-46 시즌)로 많지 않지만, UEFA 유로파 리그에선 무려 6회나 우승하여 역대 최다 우승팀이다.. ', 'league':'La Liga'},
    {'team_id':31, 'name': '레알 베티스', 'img_url': 'https://w.namu.la/s/d436f316d1791b758237451f64b28a42868a2149813b128d8d85c95349e17e48061b8766c811339969ab18caef2dff327cd5de19956f67337e8116442e9c1345c8a09f54277732e8d5f575454352abc48b5d7b725914817f1644956600e116eb', 'like': 0, 'status': '세비야 FC 와 함께 스페인 남부 안달루시아 지방을 대표하는 클럽. 흰색과 녹색 줄무늬 유니폼 색깔로 인해 베르디블랑코라는 애칭으로 불리며, 이 고유의 색깔은 스코틀랜드 셀틱으로부터 영향을 받은 것이라고 한다.', 'league':'La Liga'},
    {'team_id':32, 'name': '오사수나', 'img_url': 'https://w.namu.la/s/21f8bbb6b7072db2c3312d807fed2ed7423ec0cab00974d355f04d8ae647960e954d4cd725e3a4a172c78b7a00f816009ebbbfefb906b7c8d10d6716f77498db4aaf47fe221c395a3bc622ef7b7e70401dc78acbba09e1e75b38ff5d62da60cb', 'like': 0, 'status': '아틀레틱 클루브, 레알 소시에다드, 데포르티보 알라베스와 함께 스페인 북부 바스크 지방을 대표하는 클럽으로, 바스크계 선수들을 중심으로 팀을 구성하지만, 바스크계가 아닌 선수들의 입단에는 특별히 제한을 두지는 않는다. 전통의 붉은 유니폼 색깔로 인해 로스 로히요스라는 애칭으로 불린다', 'league':'La Liga'},
    {'team_id':33, 'name': '그라나다', 'img_url': 'https://w.namu.la/s/3b90ab89b969ec58b92ab591019d7bc7f691dd56eef24c1c2e8697ae36c800d493a50bb46f9812a996fda7aabd18f1e1362c52e983b6c5d0d92c6e8717d564ba2a5c0dacc411b48965ec9145875f14635549248234a7913eb101ff90c0020071', 'like': 0, 'status': '스페인 남부 안달루시아 지방의 중소클럽. 말라가의 오랜 더비 라이벌이며, 두 팀의 경기는 동 안달루시아 더비 혹은 오리엔탈 더비라는 이름으로 불린다. 애칭은 팀 이름을 간략히 줄인 엘 그라나. 여기엔 그라나다 전통의 붉은 유니폼을 상징하는 의미도 담겨 있다.', 'league':'La Liga'},
    {'team_id':34, 'name': '셀타비고', 'img_url': 'https://w.namu.la/s/08a79e5e6064aca90d40b75241edad103e2215b0b6efecd5d27553ffc78413631ac2aca676697ed6fb6d2fb62d669f71cfe091e3f6b2632dd454e74902ad1d119552aba52309f9d045d2d5b80f864ce6de154deb01435f8fa89ffff7f2f74d51', 'like': 0, 'status': '스페인의 축구 클럽. 프리메라 리가에 참여하고 있다. 연고 도시는 스페인 서북부 갈리시아 주의 비고(Vigo)로 포르투갈과 매우 인접한 도시이다. 스페인이나 해설가들은 주로 셀타라고 줄여부른다.', 'league':'La Liga'},
    {'team_id':35, 'name': '마요르카', 'img_url': 'https://w.namu.la/s/2203219721facc46bb567310c9281b853086b3b9109b4fb522e1c1bc436cd66e727b0759b886f8fab505265ac7e8a697934d02139cf30088c627482168d8bc07e8694a835b5e9ce824df289f174467bea47ecbffa7ac328dfb067228b099d073', 'like': 0, 'status': '스페인 라리가 소속의 프로 축구 클럽이다.', 'league':'La Liga'},
    {'team_id':36, 'name': '엘체', 'img_url': 'https://w.namu.la/s/41568e650fa0604b024e9570a938a3549786fb6e42735bad3da34326b5ee709e3b6d550f5c7d245b559fda70aad6a3243b82d006644fd4e79636b129e731356e42bf6d4267e03070fc2cb9fd9a518634d6447a0a40dee59e5af699303a28d751', 'like': 0, 'status': '스페인의 축구 팀. 라리가에 참여하고 있다. 연고 도시는 발렌시아 주의 엘체이다. 잉글리시 리그 1의 볼턴 원더러스와 제휴 관계를 맺고 있다. 최대 라이벌은 인근의 알리칸테에 있는 에르쿨레스 CF이다. 알리칸테와 접하는 무르시아 최대의 클럽인 레알 무르시아와도 약간의 라이벌 의식을 갖고 있다.', 'league':'La Liga'},
    {'team_id':37, 'name': '헤타페', 'img_url': 'https://ww.namu.la/s/ebd1d05733a96ef7590ab19670830ac372bef3708d0a51bd8d321a37fedbc396714dcce771be1fac242df458081d955f900f2ac546ceace7462018656f380b0588e0ca90278db8044334320dea200834e3a7fa93ff9e7afe42fa89aab0cf66a5', 'like': 0, 'status': '스페인의 축구 클럽. 프리메라 리가에 참가하고 있다. 연고지인 헤타페는 마드리드 남쪽에 자리한 위성도시이자 베드타운. 마드리드 지하철 12호선이 이 일대를 지나다닌다.', 'league':'La Liga'},
    {'team_id':38, 'name': '알라베스', 'img_url': 'https://w.namu.la/s/4597edaf4145aedd344b39980a93a201f118909e6d8a419af0aa03649e098f9204105b4add5d45f738d37b8365a2a59d12dc27e5e6724eb32df4cf1c57459a1f23bcf7054dc43897a898fdbe3020ce85b40506fbbc0495896cc6094d58d0cea0', 'like': 0, 'status': '데포르티보 알라베스, 약칭 알라베스는 스페인의 축구 클럽으로, 바스크 지방의 아라바 주 비토리아를 연고지로 한다. 2017-18 시즌 프리메라리가에 참가하고 있다.', 'league':'La Liga'},
    {'team_id':39, 'name': '카디스', 'img_url': 'https://w.namu.la/s/51470a77d55614d5e851d6f02147acf8c30b7f49fdd11178ded1576dae14fb64a9aa95798a95ee85162e9967ac655350d27de6accdd46cf01c96934c0e2ee4d1c0ee7326cb27f1e0031110e8109b3c4da22642f9d20a96ae5c8196d5f900d7bf', 'like': 0, 'status': '카디스 CF는 스페인 카디스의 축구 클럽이다. 현재 스페인 라리가에 소속되어 있다.', 'league':'La Liga'},
    {'team_id':40, 'name': '레반테', 'img_url': 'https://w.namu.la/s/76e77652d6724924fca2003db2ebb23f42eaf2561da2a78b1dc54ba6a79e60e6a514cdc71c37cb08f0dfee6330e4ae0a0489bddcf12ee39c24841221d88d7ce0849e41871c4fa8a2613adb2365d0324dd61f115fb636edfc14311531b3f635c0', 'like': 0, 'status': '스페인 제 3의 도시 발렌시아를 대표하는 2인자 클럽. 발렌시아 CF와는 오랜 라이벌 관계이며, 두 팀의 경기는 발렌시아 더비로 잘 알려져 있다.', 'league':'La Liga'},

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
