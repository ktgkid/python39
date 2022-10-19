# 튜플tuple
# 파이썬의 리스트와 유사한 자료구조
# 선언방법은 ()안에 값들을 정의 하고 사용
# 단, 튜플의 요소는 수정이나 삭제 불가(생성은 가능)
# 주로, 읽기전용 데이터를 다룰때 사용
nums = (1, 5, 10, 15, 20)
print(nums)

# 튜플의 요소 읽기 = 객체명[인덱스]
print(nums[0], nums[3])

# 튜플의 요소 수정: 객체명[인덱스] = 수정값 수정 처리 불가
# nums[0] = 999

# 튜플의 요소 삭제 : del 객체명[인덱스] 불가
# del nums[1]

score = [
    [10, 20, 30],
    [98, 17, 52],
    [56, 89, 97],
]

print(score[2][1])

for sc in score:
    print(sc)

# 2차원 리스트 동적 생성
# 전체 리스트 크기를 사용자로부터 입력 받음
# 요소로 사용하는 리스트의 크기는 난수로 생성
# 요소 리스트를 구성하는 값 역시 난수로 생성
import random as rnd

length = int(input("리스트 크기는"))
lsts = []

for i in range(length):
    lst = []
    for j in range(rnd.randint(1, 10)):
        lst.append(rnd.randint(100, 1000))
    lsts.append(lst)

print(lsts)

# ex) 년도를 입력하면 십간과 십이지를 이용해서 해당년도의 60갑자 출력
# 간지 : 갑을병정무기경신임계
# 십이지 : 자축인묘진사오미신유술해

ganji = ('경', '신', '임', '계', '갑', '을', '병', '정', '무', '기')
sip2ji = ('신', '유', '술', '해', '자', '축', '인', '묘', '진', '사', '오', '미')

year = int(input('연도를 입력하세요 : '))
curgan = year % 10
cursip = year % 12
print(f'{ganji[curgan]}{sip2ji[cursip]}년 입니다.')

# ex) 로또 645 : 1 ~ 45사이 임의의 숫자 6개 생성 1
# 단, set를 이용해서 같은 숫자가 출현하지 않도록 작성
import random as rnd
lotto = set()

while len(lotto) < 6:
    lotto.add(rnd.randint(1, 45))   # 중복 삽입시 값이 추가가 아닌 덮어쓰기 진행으로 set 길이는 변환 되지 않음

# ex) 로또 645 : 1 ~ 45사이 임의의 숫자 6개 생성 2
# 단, list를 이용해서 같은 숫자가 출현하지 않도록 작성
# 리스트 간소화 처리
import random as rnd
lotto = []
while len(lotto) < 6:
    num = rnd.randint(1, 45)    # 로또 번호 생성
    if not(num in lotto): lotto.append(num)     # 배열내 랜덤 생성 된 값 존재 여부에 따라 값 추가 결정

print(lotto)

# ex) 로또 645 : 1 ~ 45사이 임의의 숫자 6개 생성 2
# 단, list를 이용해서 같은 숫자가 출현하지 않도록 작성
# 강사님 요청
import random as rnd
lotto = []
rangeNum = list(range(1, 46))
while len(lotto) < 6:
    num = rnd.randint(0, len(rangeNum))     # 검색할 리스트 일련번호 무작위 생성
    lotto.append(rangeNum[num])     # 리스트 일련번호 내 값 추가
    rangeNum.pop(num)   # 삽입 된 리스트 일련번호 삭제

print(lotto)
print(rangeNum)
