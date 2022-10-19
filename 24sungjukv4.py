# 함수를 이용 성적처리 프로그램

# 함수 정의부
def displayMenu():
    menu = f'''
    성적 처리프로그램 v4
    -----------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -----------------'''
    print(menu)

def addSungJuk():
    name = input('이름은?')
    kor = int(input('국어 점수는?'))
    eng = int(input('영어 점수는?'))
    mat = int(input('수학 점수는?'))

    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'

    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    sj = {}
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

    sjs.append(sj)
    print('성적데이터 추가 완료!')

def readSungJuk():
    hdr = '이름 국어 영어 수학\n'
    hdr += '-----------------'
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]}', end=' ')
        print()
    print('성적 데이터 조회 완료!')

def readOneSungJuk():
    name = input('조회할 학생의 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name:
            sj = item

    hdr = '이름 국어 영어 수학 총점 평균 학점\n'
    hdr += '---------------------------------'
    print(hdr)

    for k in sj.keys():
        print(sj.get(k), end=' ')
    print()
    print('성적 데이터 상세조회')

def modifySungJuk():
    name = input('수정할 학생 이름은?')

    sj = None
    for item in sjs:
        if item['name'] == name:
            sj = item

    # 기존에 위치에 다시저장
    idx = None
    for i in range(len(sjs)):
        if (sjs[i])['name'] == name:
            idx = i

            # 새로운(기존) 값을 입력받음
            kor = int(input(f'새로운 국어는? {sj["kor"]}'))
            eng = int(input(f'새로운 영어는? {sj["eng"]}'))
            mat = int(input(f'새로운 수학은? {sj["mat"]}'))

            # 다시 성적 처리
            tot = kor + eng + mat
            avg = tot / 3
            grd = '가'

            if avg >= 90:
                grd = '수'
            elif avg >= 80:
                grd = '우'
            elif avg >= 70:
                grd = '미'
            elif avg >= 60:
                grd = '양'
            break
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}

    sjs[idx] = sj
    print('성적 데이터 수정')

def removeSungJuk():
    name = input('삭제할 데이터의 학생 이름은?')

    idx = None
    for i in range(len(sjs)):
        item = sjs[i]
        if item['name'] == name:
            idx = i

    sjs.pop(idx)
    print('성적 데이터 삭제')

# 성적 데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부


while True:
    # 메뉴표시 및 값 입력
    displayMenu()
    menu = input("메뉴를 선택하세요 => ")

    if menu == '1': addSungJuk()
    elif menu == '2': readSungJuk()
    elif menu == '3': readOneSungJuk()
    elif menu == '4': modifySungJuk()
    elif menu == '5': removeSungJuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력하였습니다')
