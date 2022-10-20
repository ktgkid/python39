# 컨프리헨션 comprehension
# 다양한 데이터 객체에 사용하는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원

# 파이썬에는 4가지 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
#1 ~ 10까지의 정수를 생성해서 리스트에 저장
a = list(range(1, 11))
b = []
for i in range(1, 11):
    b.append(i)
print(a)
print(b)

# 리스트 for 축약문
# [표현식 for 항목 in 반복가능 객체]
c = [i for i in range(1, 11)]
print(c)

# ex) 1 ~ 20에 정수중 짝수를 리스트로 생성
print()
print('1 ~ 20에 정수중 짝수를 리스트로 생성')
d = []
for i in range(1, 21):
    if i % 2 == 0: d.append(i)
print('----------------------------- 일반 포문 적용')
print(d)
print('-----------------------------')
print()
d = list(filter(lambda b: b % 2 == 0, range(1, 21)))
print('----------------------------- filter 적용')
print(d)
print('-----------------------------')
print()
print('----------------------------- comprehension 적용')
d = [i for i in range(2, 21, 2)]
print(d)
print('-----------------------------')
print()
# ex) 1 ~ 10사이 정수를 제곱한 값을 리스트로 생성
print('1 ~ 10사이 정수를 제곱한 값을 리스트로 생성')
print()
e = []
for i in range(1, 11):
    e.append(i**2)
print('----------------------------- 일반 포문 적용')
print(e)
print('-----------------------------')
print()
e = list(map(lambda b: b**2, range(1, 11)))
print('----------------------------- map 적용')
print(e)
print('-----------------------------')
print()
e = [i**2 for i in range(1, 11)]
print('----------------------------- comprehension 적용')
print(e)
print('-----------------------------')
# d = {i for i in range(1, 11)}
# print(d)

# ex) 아래 각각의 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성 하세요
val1 = [1, 2, 3, 4, 5]
f = []
for i in val1:
    if type(i) == int : f.append(i**2)
    else: f.append(i)
print('----------------------------- 일반 포문 적용')
print(f)
print('-----------------------------')
print()
f = list(map(lambda b: b**2 if type(b) == int else b, val1))
print('----------------------------- map 적용')
print(f)
print('-----------------------------')
print()
f = [b**2 if type(b) == int else b for b in val1]
print('----------------------------- comprehension 적용')
print(f)
print('-----------------------------')
print()

val2 = [1, 2, 'A', False, 9, 100]
g = []
for i in val2:
    if type(i) == int : g.append(i**2)
#    else: g.append(i)
# for if 축약문
# [표현식 for 항목 in 반복가능객체 if 조건]
print('----------------------------- 일반 포문 적용')
print(g)
print('-----------------------------')
print()
g = list(map(lambda b: b**2 if type(b) == int else b, val2))
print('----------------------------- map 적용')
print(g)
print('-----------------------------')
print()
g = [b**2 for b in val2 if type(b) == int]
print('----------------------------- comprehension for if 적용')
print(g)
print('-----------------------------')
g = [b**2 if type(b) == int else b for b in val2]
print('----------------------------- comprehension 삼항 연산식 적용')
print(g)
print('-----------------------------')
print()

# 1 ~ 60 사이 정수 중 홀수만 골라 리스트에 저장
h = [i for i in range(1, 60, 2)]
print('----------------------------- comprehension')
print(h)
print('-----------------------------')
h = [i for i in range(1, 60) if i % 2 != 0]
print('----------------------------- comprehension for if 적용')
print(h)
print('-----------------------------')

# 1 ~ 60 사이 정수 중 5의 배수만 골라 리스트에 저장
j = [i for i in range(5, 60, 5)]
print('----------------------------- comprehension')
print(j)
print('-----------------------------')

j = [i for i in range(1, 60) if i % 5 == 0]
print('----------------------------- comprehension for if 적용')
print(j)
print('-----------------------------')

# ex) 1~100 사이 정수중에서 임의의 정수가 짝수면 'even'
# 홀수면 'odd' 라고 구분해서 리스트에 저장
k = [f'{i}:even' if i % 2 == 0 else f'{i}:odd' for i in range(1, 101)]
print(k)

# ex) 구구단 중 7, 8단의 결과값을 리스트에 저장
l = [f'{i} x {j} = {i * j}' for i in range(7,9) for j in range(1, 10)]
print(l)

# ex) name, grd 리스트의 값들을
# 각각의 키와 값으로 딕셔너리에 저장
name = ['혜교','지현','수지']
grd = ['우','미','수']

# 단순하게 작성
# 새로운 dict요소 생성 : 객체명[키이름] = 값
s = {}
s[name[0]] = grd[0]
s[name[1]] = grd[1]
s[name[2]] = grd[2]

print(s)
# 반복문 작성
s = {}
for i in range(len(name)):
    s[name[i]] = grd[i]

print(s)
#print({name, grd})
# 딕셔너리 for 축약문
# { for k, v in zip(반복가는객체1, 반복가능객체2)}
print(dict(zip(name, grd)))
print({name[i]:grd[i] for i in range(len(name))})
print({k:v for k,v in zip(name, grd)})

# ex) 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 합격여부를 값으로 하는 딕셔너리 객체를 생성
# 단, 합격여부에는 국어점수가 85점이상인 경우 '합격'
# 그외는 '불합격'이라고 출력함
name = ['철수','영희','길동','꺽정']
kor = [50, 80, 90, 60]
t = {}
for i in range(len(name)):
    val = '합격' if kor[i] >= 85 else '불합격'
    t[name[i]] = val
print(t)
print({k:"합격" if v >= 85 else "불합격" for k,v in zip(name, kor)})

# 딕셔너리 for if 축약문
# { 키: 표현식1 if 조건식 else 표현식2
# for k, v in zip(반복가는 객체1, 반복가능객체2)}

# p111 ex3)
# A) spam은 1로 ham은 0으로 생성하는 dummy 변수 생성
message = ['spam', 'ham', 'spam', 'ham', 'spam']
dummy = [1 if i == 'spam' else 0 for i in message]
print(dummy)

dummy = list(map(lambda i: 1 if i == 'spam' else 0, message))
print(dummy)

# B) spam 원소만 추출
dummy = [i for i in message if i == 'spam']
print(dummy)

def makeDummy(x):
    val = 0
    if x == 'spam': val = 1
    return val

print(list(map(makeDummy, message)))

def getSpam(x):
    return x == 'spam'

print(list(filter(getSpam, message)))
print(list(filter(lambda x:x == 'spam', message)))
