# ex) 60갑자를 출력해주는 프로그램을 함수로 작성
# 함수명 : checkChinaZodiac(년도) # 4-123p

def checkChinaZodiac(year):
    baseYear = 1444
    ten = ('갑', '을', '병', '정', '무', '기', '경', '신', '임', '기')
    twelve = ('신', '유', '술', '해', '자', '축', '인', '묘', '진', '사', '오', '미')
    animal = ('쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양', '원숭이', '닭', '개', '돼지')

    t10idx = (year - baseYear) % 10
    t12idx = (year - baseYear) % 12

    print(f'{year}년은 {ten[t10idx]}{twelve[t12idx]}년'
          f'({animal[t12idx]}의 해)입니다')

    year = int(input('년도는?'))
    checkChinaZodiac(year)
