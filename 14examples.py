# p78 ex2) 숫자 맞추기(1~10)
import random as rnd

print('>>숫자 맞추기 게임<<')
com = rnd.randint(1, 10)    # 1~10 난수 발생

while True:
    my = int(input('예상 숫자를 입력하시오 : '))  # 숫자입력
    if com == my:
        print('~~~성공~~~')
        break
    elif com >= my:
        print('더 큰 수 입력~')
        continue
    elif com <= my:
        print('더 작은 수 입력~')
        continue

import random as rnd

magic = rnd.randint(1, 10)

while True:
    key = input('숫자를 하나 입력하세요')

    if magic == key: print('성공')
    elif magic > key: print('숫자가 커요')
    else: print('숫자가 작아요')

# ex30) 숫자 맞추기(1~100)
import random as rnd

num1 = rnd.randint(1, 100)

while True:
    num2 = input('숫자를 하나 입력하세요')

    if num1 < num2:
        print('숫자가 커요')
        break
    elif num1 > num2: print('숫자가 작아요')
    else: print('빙고 성공~')

# ex25) 복권 프로그램 ~ 3자리수 난수 생성/사용자 입력
# 난수 범위 - 100~999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 -> 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 변환 str 함수 사용
# 3개 일치 - 상금 백만원!
# 2개 일치 - 상금 5만원!
# 1개 일치 - 상금 1천원!
# 0개 일치 - 다음 기회에!
import random as rnd

print('>>Lotto~~~<<')
lotto = rnd.randint(100, 999)
# lotto1 = str(rnd.randint(1, 9))
# lotto2 = str(rnd.randint(1, 9))
# lotto3 = str(rnd.randint(1, 9))
# lotto = lotto1 + lotto2 + lotto3

# print(lotto)
#
# while True:
#     my = int(input('복권세자리번호입력 : '))
#     if lotto[3:] == my:
#         print(f'3개 일치 - 상금 백만원!, {lotto}({[1:0]})')
#     elif lotto[2:] == my:

mykey = input('3자리 입력')
match = 0   # 일치여부 저장
# # 첫째 자리 비교
# if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
#     match += 1
# # 둘째 자리 비교
# if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
#     match += 1
# # 셋째 자리 비교
# if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
#     match += 1
# # 개선된 코드 1
# for i in range(3):
#     if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[0] == mykey[2]:
#         match += 1
# # 개선된 코드 1b
# for i in range(3):
#     if lotto[i] == mykey[0]: match += 1
#     if lotto[i] == mykey[1]: match += 1
#     if lotto[i] == mykey[2]: match += 1
# 개선된 코드 2
for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j]: match += 1

# 당첨여부판단
if match == 3: print('3개 일치 - 상금 백만원!')
elif match == 3: print('2개 일치 - 상금 5만원!')
elif match == 3: print('1개 일치 - 상금 1천원')
else: print('꽝')