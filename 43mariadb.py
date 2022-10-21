# mariaDB 로 데이터 다루기 1 - select
# pymysql 모듈을 먼저 설치 : pip install pymysql
import pymysql

url = 'bigdata.cv4zpe7xozml.ap-northeast-2.rds.amazonaws.com'
userid = 'admin'
passwd = 'Bigdata_2022'
dbname = 'bigdata'

conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')

cur = conn.cursor()
sql = 'select userid, passwd, name, email from member'
cur.execute(sql)

result = ''
rows = cur.fetchall()       # 실행결과집합 모두 가져옴
for row in rows:
    result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'    # 출력결과 누적

cur.close()
conn.close()
print(result)

# mariaDB 로 데이터 다루기 2 - insert
import pymysql

uid = input('아이디는?')
pwd = input('비밀번호는?')
name = input('이름은?')
email = input('이메일은?')

conn = pymysql.connect(host=url, user=userid, password=passwd, database=dbname, charset='utf8')

cur = conn.cursor()
sql = 'select userid, passwd, name, email from member'
cur.execute(sql)

# 매개변수 placeholder(%) 를 이용해서 실제 값 지정
sql = f' insert into member (userid, passwd, name, email) values (%s, %s, %s, %s) '
params = (uid, pwd, name, email)

cur.execute(sql, params)
conn.commit()        # 테이블에 값 저장하기 위해 commit 호출
print(cur.rowcount, '행이 추가됨!')

cur.close()
conn.close()