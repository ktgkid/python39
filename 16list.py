# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 변수 초기화
name1, name2, name3 = '혜교', '지현', '수지'
kor1, kor2, kor3 = 99, 65, 75
# ...
# 처리할 데이터 갯수에 따라 변수를 일일히 선언해야 함 - 불편!
# tot1 = kor1 + eng1 + mat1
# tot2 = kor2 + eng2 + mat2
# tot3 = kor3 + eng3 + mat3
# ...
# 성적처리시에도 동일한 코드를 여러번 반복해 작성함 - 번거로움
# => 이러한 문제를 해결하기 위해 자료구조와 관련된 기술을 사용

# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복 허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근하려면 변수[인덱스] 형식을 사용

# 점심메뉴를 리스트로 정의
menus = ['라면', '돈까스', '짜장면', '냉면', '정식']
print(menus)

# 리스트에서 일부요소만 출력
print(menus[0], menus[2], menus[4])

# 리스트의 모든 요소 출력
print(menus[0], menus[1], menus[2], menus[3], menus[4])

# 리스트의 모든 요소를 반복문으로 출력 1
# for i in range(5):
for i in range(len(menus)):     # len(대상) : 요소 갯수 출력
    print(menus[i], end=' ')

# 리스트의 모든 요소를 반복문으로 출력 2
# for 변수 in 객체
for menu in menus:      # 리스트의 요소를 하나씩 훑어가며 출력
    print(menu, end=' ')

# 동적으로 리스트 생성하기
menu = []       # 빈 리스트 선언

# 리스트에 요소를 추가하려면 append 함수
# append 한 요소는 리스트의 맨 뒤에 부착 - FIFO
menus.append('라면')
menus.append('돈까스')
menus.append('짜장면')
menus.append('우동')
menus.append('정식')

# 지정한 위치에 새로운 요소 추가 : append(인덱스, 값)
# 지정한 인덱스에 이미 값이 존재하면 그 값은 뒤로 밀림
menus.insert(3, '냉면')

# 리스트 요소의 값 수정 : 객체명[인덱스] = 새로운 값
print(menus[3])
menus[3] = '탕수육'

# 리스트 요소 삭제 : remove(값) - 값으로 삭제
menus.remove('탕수육')

# 리스트 요소 삭제 : pop(값) - 위치로 삭제
menus.pop(2)

# 리스트 요소 삭제 : pop(값) - 위치로 삭제, 뒤에서 부터 삭제
menus.pop()

# 리스트로 다양한 데이터 다루기
datas = []

datas.append(1)
datas.append(2.5)
datas.append(True)
datas.append('Hello')
datas.append([1, 3, 5, 7, 9])

print(datas)

# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함

# 변수 선언/초기화
names = ['혜교', '지현', '수지']
kors = [99, 54, 65]
engs = [76, 77, 87]
mats = [87, 77, 90]
tots = [0, 0, 0]
avgs = [0, 0, 0]
grds = ['가', '가', '가']
# 성적처리 1
tots[0] = kors[0] + engs[0] + mats[0]
tots[1] = kors[1] + engs[1] + mats[1]
tots[2] = kors[2] + engs[2] + mats[2]

avgs[0] = tots[0] / 3
avgs[1] = tots[1] / 3
avgs[2] = tots[2] / 3

if avgs[0] >= 90: grds[0] = '수'
elif avgs[0] >= 80: grds[0] = '우'
elif avgs[0] >= 80: grds[0] = '미'
elif avgs[0] >= 80: grds[0] = '양'

if avgs[1] >= 90: grds[1] = '수'
elif avgs[1] >= 80: grds[1] = '우'
elif avgs[1] >= 80: grds[1] = '미'
elif avgs[1] >= 80: grds[1] = '양'

if avgs[2] >= 90: grds[2] = '수'
elif avgs[2] >= 80: grds[2] = '우'
elif avgs[2] >= 80: grds[2] = '미'
elif avgs[2] >= 80: grds[2] = '양'
# 결과출력 1
print(names[0], kors[0], engs[0], mats[0], tots[0], avgs[0], grds[0])
print(names[1], kors[1], engs[1], mats[1], tots[1], avgs[1], grds[1])
print(names[2], kors[2], engs[2], mats[2], tots[2], avgs[2], grds[2])
# 성적처리 2
for i in range(len(names)):
    tots[i] = kors[i] + engs[i] + mats[i]
    avgs[i] = tots[i] / 3
    if avgs[i] >= 90: grds[i] = '수'
    elif avgs[i] >= 80: grds[i] = '우'
    elif avgs[i] >= 80: grds[i] = '미'
    elif avgs[i] >= 80: grds[i] = '양'
# 결과출력 2
for i in range(len(names)):
    print(names[i], kors[i], engs[i], mats[i], tots[i], avgs[i], grds[i])

# p110 ex1)
lst = [10, 1, 5, 2]     # list 생성
# lst 를 2배 생성 후 result 에 저장 1
result = lst
result += lst
print(result)
# lst 를 2배 생성 후 result 에 저장 2
result = []
for _ in range(2):
    result += lst
print(result)
# lst 를 2배 생성 후 result 에 저장 3
# 리스트에 * 연산자 적용 -> 복제 적용
result = []
result = lst * 2
print(result)
# lst 의 첫번째 요소에 * 2 한 후 result 에 저장
# result.append(lst[0] * 2)
val = lst[0] * 2
result.append(val)
# result 리스트에서 홀수요소만 추출 1 -> result2 에 저장
result2 = []
result2.append(result[1])
result2.append(result[3])
result2.append(result[5])
result2.append(result[7])
print(result2)
# result 리스트에서 홀수요소만 추출 2
result2 = []
# for i in range(1, 9, 2):    # 1, 3, 5, 7
for i in range(1, len(result), 2):
    result2.append(result[i])
print(result2)
# result 리스트에서 홀수요소만 추출 3 - list slice
result2 = result[1::2]
print(result2)

# p110 ex2) A
import random as rnd

lst = []
size = int(input('리스트의 크기는?'))
for i in range(size):
    val = rnd.randint(1, 10)
    print(val)
    lst.append(val)
print(f'리스트의 크기 : {len(lst)}')

# p110 ex2) B
import random as rnd

lst = []
size = int(input('리스트의 크기는?'))
for i in range(size):
    val = rnd.randint(1, 10)
    print(val)
    lst.append(val)
key = int(input('리스트에서 찾을 값은?'))
# 검색기능 1
isFind = 'NO'
for i in range(size):
    if lst[i] == key: isFind = 'YES'
print(isFind)
# 검색기능 2
isFind = 'NO'
for val in lst:
    if val == key: isFind = 'YES'
print(isFind)
# 검색기능 3 : if 값 in 객체 - 객체에서 특정값 존재 여부 확인
isFind = 'NO'
if key in lst: isFind = 'YES'
print(isFind)

# employees.csv를 이용해서 사원정보를 입력하면
# list에 각각 저장하는 코드를 작성하세요
# 사번empno, 이름fname, 성lname, 이메일email,
# 입사일hdate, 직책jobid, 급여sal, 부서번호deptid
empnos = []
fnames = []
lnames = []
emails = []
hdates = []
jobids= []
sals = []
deptids = []

empno = input('사원번호는?')
fname = input('이름은?')
lname = input('성은?')
email = input('이메일은?')
hdate = input('입사일은?')
jobid = input('직책은?')
sal = input('급여는?')
deptid = input('부서번호는?')

empnos.append(empno)
fnames.append(fname)
lnames.append(lname)
emails.append(email)
hdates.append(hdate)
jobids.append(jobid)
sals.append(sal)
deptids.append(deptid)
# 저장된 모든 사원정보 출력
for i in range(len(empnos)):
    print(f'{empnos[i]}, {fnames[i]}, {lnames[i]},'
          f'{emails[i]}, {hdates[i]}, {jobids[i]},'
          f'{sals[i]}, {deptids[i]}')
# 다루어야 하는 데이터의 항목수가 많을 수록 일일이 리스트로 선언해서 저장하는 것은 다소 불편
# => dictionary, class 를 이용하면 편리하게 다룰 수 있음
