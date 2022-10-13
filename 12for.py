# for (int i = 0; i <= 9; ++i){
# }
# for i in range(0, 10):  # 0~9

# for i in 0,1,2,3,4,5,6,7,8,9:
#     코드

# 반복문
# 정해진 횟수 만큼 특정코드를 실행하도록 만든 문장
# 파이썬 에서는 for 문과 while 문이 지원

print('Hello, World!!')     # 한번 출력

print('Hello, World!!')     # 3번 출력
print('Hello, World!!')
print('Hello, World!!')

# 만일, 100번 출력해야 한다면 복붙을 계속할 것인가?
# 또한, 반복시 출력하는 문구가 변경된다면? - 다시 수정
# 효율적인 반복실행을 위해서 반복문을 사용함

# for 반복변수 in range(시작값, 종료값-1, 증감값):
#     반복실행할 문장

# range 함수 사용하기
# range(숫자) - 0 부터 숫자 -1 까지의 범위
list(range(10))     # 0~(10-1) 범위

# range(시작, 끝-1) - 시작값부터 끝값-1 까지의 범위
list(range(1, 45+1))

# range(시작, 끝-1, 증감값)
# => 시작값에서 증감값을 처리해서 끝값-1의 범위까지 출력
list(range(1, 10, 2))
list(range(0, 10, 2))

# ex) 1~100
# 반복문을 이용한다면?
list(range(1, 100+1))

for i in range(1, 100+1):
    print(i, end=', ')      # 출력문 줄바꿈 하지 않기
# print 함수로 값 출력시 줄바꿈 문자가 자동 추가됨
# 줄바꿈 문자대신 다른 문자로 대신하려면 end 속성 사용

# ex) 100~1
# for i in range(1, 100+1):
#     print(i, end=', ')
list(range(100, 0, -1))
for i in range(100, 0, -1):
    print(i, end=', ')

# ex) 1~100 사이 정수 중 짝수만 출력
list(range(2, 100+1, 2))
for i in range(2, 100+1, 2):
    print(i, end=', ')

list(range(1, 100+1))
for i in range(1, 100+1):
    if i % 2 == 0: print(i, end=' ')

# 1~100 사이 정수들의 모든 합 계산 출력
isum = 0
for i in range(1, 100+1):
    isum = isum + i
print(isum)

# 가우스 덧셈 공식을 이용해서
# 1~100 사이 정수들의 모든 합 계산 출력
# x~y 까지의 숫자를 더한 합을 구하는 공식
# ((x + y) * (y - x + 1)) /2
((1 + 100) * (100 - 1 + 1)) / 2

range(1, (100+1)*50)

sum = 0
for i in range(1, 51):  # 1~100 사이에서 모든 쌍의 합의 전체 개수의 절반인 50개
    sum += i + (101 - i)
print(sum)

# 문자열에 반복문 적용하기
# => 문자열에서 문자를 하나씩 가져와서 출력함
for i in 'Hello, World!!':
    print(i, end=' ')

# ex) 단을 입력받아 해당 단의 구구단 출력
dan = int(input('단?'))
for i in range(1, 9+1):
    print(f'{dan} x {i} = {dan * i}')

# p79 ex3) 3의 배수지만 2의 배수는 아닌 정수 출력하고 누적합도 계산해서 출력 (1~100)
hap = 0
result = ''
for i in range(1, 100+1):
    if i % 3 == 0 and i % 2 != 0:
        result += str(i) + ' '
        hap += + i

print(result)
print(hap)
