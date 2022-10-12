# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서
# 각 변수에 적절히 저장하세요.
jumin = '202205092123456'

# year = print(jumin[0:4])
# month = print(jumin[4:6])
# day = print(jumin[6:8])
# gender = print(jumin[8])

# print(f'''
# year = {jumin[0:4]}
# month = {jumin[4:6]}
# day = {jumin[6:8]}
# gender = {jumin[8]}
# ''')

year = jumin[0:4]
month = jumin[4:6]
day = jumin[6:8]
gender = jumin[8]

print(year, month, day, gender)

# 14 - 시간계산
day = 86400
num1 = 1234567890
total = num1 // day   # 정수부분만 추출 ( // )
print(total)

hour = 3600
num2 = 98765
tothour = num2 // hour
print(tothour)

min = 60
num3 = 12345
totmin = num3 // min
print(totmin)

# 16 - 잔돈계산
# 비용과 지불금액을 입력받아 잔돈 계산
# 지불금액은 ???원 이고, 받은 금액은 ???원 이고, 잔액은 ???원 입니다.
# 50,000원권은 ?장, 10,000원권은 ?장, 5,000원권은 ?장, 1,000원권은 ?장, 500원은 ?개, 100원은 ?개, 50원은 ?개, 10원은 ?개 입니다.
amount = int(input('입력금액 :'))
price = int(input('가격 :'))
charge = amount - price
# a = charge // 50000
# b = (charge - (50000 * a)) // 10000
# c = (charge - (50000 * a + 10000 * b)) // 5000
# d = (charge - (50000 * a + 10000 * b + 1000 * c)) // 1000
# e = (charge - (50000 * a + 10000 * b + 1000 * c + 500 * d)) // 500
# f = (charge - (50000 * a + 10000 * b + 1000 * c + 500 * d + 100 * e)) // 100
# g = (charge - (50000 * a + 10000 * b + 1000 * c + 500 * d + 100 * e + 50 * f)) // 50
# h = (charge - (50000 * a + 10000 * b + 1000 * c + 500 * d + 100 * e + 50 * f + 10 * g)) // 10
a = charge // 50000
b = charge % 50000 // 10000
c = charge % 10000 // 5000
d = charge % 5000 // 1000
e = charge % 1000 // 500
f = charge % 500 // 100
g = charge % 100 // 50
h = charge % 50 // 10
print(f'''
지불금액은 {price}원이고, 받은 금액은 {amount}원이고, 잔액은 {charge}원
50,000원권은 {a}장, 
10,000원권은 {b}장, 
5,000원권은 {c}장, 
1,000원권은 {d}장, 
500원은 {e}개, 
100원은 {f}개, 
50원은 {g}개, 
10원은 {h}개 입니다.
''')

# 파이썬에서 제공하는 몫/나머지 연산자를 이용하면 수식이 좀 더 간단해짐

price = int(input('판매가를 입력해주세요'))
inMoney = int(input(f'''지불금액을 입력해 주세요'''))
difference = inMoney - price
balance = 0

cash = 50000
fiftyThou = int((difference - balance) / cash)
balance += fiftyThou * cash

cash = 10000
tenThou = int((difference - balance) / cash)
balance += tenThou * cash

cash = 5000
fiveThou = int((difference - balance) / cash)
balance += fiveThou * cash

cash = 1000
oneThou = int((difference - balance) / cash)
balance += oneThou * cash

cash = 500
fiveHund = int((difference - balance) / cash)
balance += fiveHund * cash

cash = 100
oneHund = int((difference - balance) / cash)
balance += oneHund * cash

cash = 50
fifty = int((difference - balance) / cash)
balance += fifty * cash

cash = 10

# 반복문 활용
price = int(input('판매가를 입력해주세요'))
inMoney = int(input(f'''지불금액을 입력해 주세요'''))
difference = inMoney - price
balance = 0

balance = 0
for cash in [50000, 10000, 5000, 1000, 500, 100, 50, 10] :
    charge = (difference - balance) // cash
    balance += charge * cash
    print(f"{cash}원권은 {charge}장")