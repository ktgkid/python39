# 33 - 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 checkCredit(코드)
# dict 자료구조를 이용해서 작성
card_info = {
    35: {
        'name': 'JCB카드',
        'company_info': {
            '6317': 'NH농협카드',
            '6901': '신한카드',
            '6912': 'KB국민카드',
        },
    },
    4: {
        'name': '비자카드',
        'company_info': {
            '04825': '비씨카드',
            '38676': '신한카드',
            '57973': '국민은행',
        },
    },
    5: {
        'name': '마스타카드',
        'company_info': {
            '15594': '신한카드',
            '24353': '외환카드',
            '40926': '국민은행',
        },
    },
}
def checkCredit(code):
    if card_info.get(int(code[:2])):    # 입력 받은 코드 앞 2자리 카드종류 여부 확인
        print(card_info[int(code[:2])]['name'])     # 코드 앞 2자리 카드종류가 존재시 카드종류 출력
        if card_info[int(code[:2])]['company_info'].get(code[2:]):  # 코드 앞 2자리 제외 코드가 카드 타입 내 카드사 존재 여부 확인
            print(card_info[int(code[:2])]['company_info'][code[2:]])   # 존재시 카드사 출력
        else: print('존재하지 않는 카드사 입니다.')     # 미존재시 카드사 없음 출력
    elif card_info.get(int(code[0])):   # 입력 받은 코드 앞 1자리 카드종류 여부 확인
        print(card_info[int(code[0])]['name'])  # 코드 앞 1자리 카드종류가 존재시 카드종류 출력
        if card_info[int(code[0])]['company_info'].get(code[1:]):   # 코드 앞 1자리 제외 코드가 카드 타입 내 카드사 존재 여부 확인
            print(card_info[int(code[0])]['company_info'][code[1:]])    # 존재시 카드사 출력
        else: print('존재하지 않는 카드사 입니다.')     # 미존재시 카드사 없음 출력
    else: print('존재하지 않는 카드 종류 입니다.')   # 카드타입 미존재시 출력

checkCredit('404825')
