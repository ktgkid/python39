# 33
# cardNum = int(input('니 카드번호 적어~'))
# jcb = 356000 <= 356999
# bisa = 400000 <= 459999
#
# nh = 356300 <= 356900
#
# # if cardNum == jcb:
# #     356300 <= 356900
# #     result = f'NH농협카드 입니다'
# # elif cardNum == jcb:
# #     356901 <= 356911
# #     result = f'신한카드 입니다'
# # elif cardNum == jcb:
# #     356912 <= 356999
# #     result = f'KB국민카드 입니다'
#
# if cardNum <= jcb:
#     nh = 356300 <= 356900
#     result = f'NH농협카드 입니다'

card = input('니 카드번호 적어~')  # 문자열 슬라이싱 slicing 이용
result = ''

if card[:2] == '35':
    nums = card[2:]  # 나머지 카드 번호 추출
    if nums == '6317':
        result = 'NH농협 JCB카드'
    elif nums == '6901':
        result = '신한 JCB카드'
    elif nums == '6912':
        result = 'KB국민 JCB카드'
elif card[:1] == '4':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '04825':
        result = 'NH농협 JCB카드'
    elif nums == '38676':
        result = '신한 JCB카드'
    elif nums == '57973':
        result = 'KB국민 JCB카드'
elif card[:1] == '5':
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '15594':
        result = 'NH농협 JCB카드'
    elif nums == '24353':
        result = '신한 JCB카드'
    elif nums == '40926':
        result = 'KB국민 JCB카드'
else:
    result = '잘못된 카드번호입니다.'

print(result)

# 35 - 시간때를 의미하는 영단어 판별
daytime = input('시간때를 의미하는 영단어는?')
result = '잘못입력하셨습니다.'

if daytime == 'morning hours':
    result = '아침시간 (7~12)'
# elif daytime == 'midday' or daytime == 'noon':
#     result = '점심시간'
elif daytime in ('midday', 'noon'):
    result = '점심시간 (12~1)'
elif daytime == 'afternoon hours':
    result == '오후 (1~6)'
elif daytime == 'evening hours':
    result == '저녁시간 (6~9)'
elif daytime == 'midnight':
    result == '밤시간 (9~12)'
elif daytime == 'early morning hours':
    result == '새벽시간 (12~5)'
elif daytime == 'small hours':
    result == '새벽 (1~3)'
elif daytime in ('dawn', 'daybreak'):
    result == '해뜰력 (5~7)'

print(result)

# switch ~ case 와 비슷하게 작성해보기
# 파이썬은 지금까지(~v3.9) switch ~ case 구문을 지원하지 않음
# 만일, switch ~ case 구문을 구현하려면 dict 를 이용해야 함
# 한편, v3.10 이상부터는 match case 라는 구문으로 구현가능

# dict 자료구조
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 = {키:값} => 객체명.get(키), 객체명[키]

cards = {'356317': 'NH농협 JCB카드', '404825': '비씨Visa카드', '515594': '신한Master카드'}
cards.get('404825')

daytime = {'midday': '점심시간', 'midnight': '자정시간', 'small hours': '새벽'}
daytime.get('midnight')

# 성적처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 계산하고 출력함
# 학점처리 조건은 수우미양가로 함
# 학점은 dict 를 이용해서 처리함
name = input('이름이 뭐니?')
kor = int(input('국어 몇?'))
eng = int(input('영어 몇?'))
mat = int(input('수학 몇?'))

tot = kor + eng + mat
avg = tot / 3
int_avg = int(avg)
unit = {}

# if int_avg >= 90: unit = '수'
# elif int_avg >= 90: unit = '우'
# elif int_avg >= 70: unit = '미'
# elif int_avg >= 60: unit = '양'
# else: unit = '가'

unit = {10: '수', 9: '수', 8: '우', 7: '미', 6: '양'}
unit = unit.get(avg // 10)

print(f"""
이름 : {name}
국어 : {kor}, 영어 : {eng}, 수학 : {mat}
총점 : {tot}, 평균 : {int(avg)}({avg:.2f})
학점 : {unit}
""")

# 3항 연산자 - if 단축문 : 컴프리헨션
# 참 일때 값 if 조건식 else 거짓일때 값
print('참' if True else '거짓')
print('참' if False else '거짓')

# ex) 윤년여부를 출력하는 프로그램을 작성하세요
# 단, 3항 연산자를 이용해서 구현함

# year = int(input('년도는?'))

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(year, '는 윤년입니다')
# else:
#     print(year, '는 윤년이 아닙니다')
year = int(input('년도는?'))
isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
result = year, '윤년입니다' if isLeapYear else '윤년이 아닙니다'

print(year, result)

# ex) 년도와 월을 입력받아 윤년여부와 입력한 달의 마지막 날을 출력하는 프로그램을 작성하세요
# 30 : 4, 6, 9, 11
# 31 : 1, 3, 5, 8, 10, 12
# 28 : 2 (윤년이 아닐 때)
# 29 : 2 (윤년일 때)
year = 2022
month = 10
