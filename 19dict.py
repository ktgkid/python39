# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 { 키:값 } 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

# dict 선언
member = {'userid': 'abc123', 'passwd': '987zxc'}

# dict 조회: 객체명['키명'], 객체명.키명
print(member['userid'])

# dict 모든 키 조회: 객체명.keys() => list 형 반납
print(member.keys())

print('------------------- 키조회')
for member_key in member.keys():
    print(member_key)
print('-------------------')
print('------------------- 값조회')
for member_value in member.values():
    print(member_value)
print('-------------------')
print('------------------- 키로 값 조회')
for member_key in member.keys():
    print(member[member_key])
print('-------------------')

print('------------------- 키, 값 조회')
for key, value in member.items():
    print(key, ' : ', value)
print('-------------------')

# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불)
def computeCharge(price, inMoney):
    difference = inMoney - price
    balance = 0

    print(
        f"""
    지불 금액은 {price}원 이고,
    받은 금액은 {inMoney}원 이고,
    잔액은 {difference}원 입니다.
    """)

    for cash in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        charge = (difference - balance) // cash
        balance += charge * cash
        print(f"{cash}원권은 {charge}장")

computeCharge(17500, 100000)
