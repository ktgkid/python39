# 변수
# 어떠한 값을 저장하는 장소를 기억하기 쉽게
# 문자형태로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라 함
# 변수에 값을 넣으라고 선언하면,
# 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제주소와 이름을 매핑함

# 이름과 나이를 저장하는 변수 선언
name = "홍길동"
age = 99

# 변수에 저장된 값을 출력하려면 print 함수 사용
print(name, age)

# 여러 문장을 한줄에 표시하려면 ";" 이용. (가독성 저하 - 비추)
name = "성춘향"; age = 45

# 변수명은 대소문자 구분
Name = "일지매"

print(name, Name)

# 파이썬의 자료형(data-type)
# 정적 타임 : 변수 선언시 자료형도 같이 표시
#           (String name = "홍길동")
#           (name = 123) (오류발생-선언시 자료형과 값의 유형이 다름)
# 동적 타임 : 변수 선언시 자료형은 생략 가능, 추론기능으로 자동할당,
#           또한, 변수에 대합사는 값에 따라 자료형이 바뀜
#           (name = '홍길동')
#           (name = 123) (문제없음-변수의 자료형은 자동으로 변경)

# 변수의 자료형을 알아보기 위해 type 함수 사용
print(type(name))

name = 123
print(type(name))

# ex) 회원정보 저장용 변수 선언
# 아이디, 비번, 이름, 나이, 이메일, 결혼여부, 통장잔액, 등록일
userid = "ktgkid"
passwd = "1234"
userName = "김태건"
Age = 36
email = "ktgkid@naver.com"
isMarried = True
hasMoney = "10000000000000"
regdate = "2022-10-11 14:39"

print(userid, passwd, userName, Age, email, isMarried, hasMoney, regdate)

# 파이썬 자료형 - 정수, 실수, 문자, 불
# 정수 자료형 - 소수점 이하의 값이 없는 수
int1 = 123
int2 = 0o010101010      # 2진수
int3 = 0o54             # 8진수
int4 = 0x7F5D           # 16진수

# 2/8/16 진수는 print 함수 사용시 10진수로 출력
print(int1, int2, int3, int4)

# 2/8/16 진수로 출력하려면 bin, oct, hex 함수등을 이용함
print(int2, bin(int2))
print(int3, oct(int3))
print(int4, hex(int4))

# 문자 자료형
# 긴 문장은 여러줄로 나눠 작성
str1 = "내려갈 때 \
보았네 \
올라갈 때 못 본 \
그 꽃"
print(str1)

# 여러 줄에 걸쳐 작성한 문자열 출력
# 줄바꿈 유지
str2 = """내려갈 때 
보았네
올라갈 때 
못 본 
그 꽃"""
print(str2)

# 문자열 슬라이싱 slicing
# 문자열은 각각의 문자들로 구성되어 있음
# 인덱스를 통해 개별 문자에 접근 가능
# 또한, : 를 이용해서 부분문자열 참조 가능
str3 = 'Hello, World!!'

print(str3[0], str3[7])         # 왼 -> 오
print(str3[-7], str3[-14])      # 오 -> 왼

print(str3[0:5], str3[:5])                # 변수명[시작:끝-1]
print(str3[7:14], str3[7:])

# len 함수 사용시 문자열의 길이 출력
len(str3)

# 부울 자료형 - 참/거짓을 나타내는 자료값
# True, False 등으로 표현
# 숫자와 0 이거나 빈 문자열이면 False 로 표현
