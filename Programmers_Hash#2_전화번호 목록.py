# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)


#     for p1, p2 in zip(phoneBook, phoneBook[1:]):  #phonebook의 첫번째 원소와 그 다음원소를 zip으로 묶어 p2가 p1으로 시작하면 return
#         if p2.startswith(p1):
#             return False
#     return True


# def solution(phone_book):
#     for i in range(len(phone_book)):
#         pivot = phone_book[i]     # phonebook의 i 번째 원소를 피봇으로 설정
#         for j in range(i+1, len(phone_book)):     # i+1 번째 원소부터 phonebook을 순회하는 j
#             strlen = min(len(pivot), len(phone_book[j]))  # 피봇과 j중 짧은 문자열의 길이를 strlen에 저장
#             if pivot[:strlen] == phone_book[j][:strlen]:  # 피봇과 j의 문자열을 strlen만큼 비교
#                 return False
#         return True


def solution(phone_book):
    hash_map = {}
    for number in phone_book:   # number를 키로 hash_map 딕셔너리를 생성
        hash_map[number] = 1
    for number in phone_book:
        temp = ""
        for i in number:        # phone_book을 순회
            temp += i           # phone_book의 원소 number의 원소를 하나씩 temp에 추가
            if temp in hash_map and temp != number:     # temp가 hash_map에 있고 number와 같지않은지 확인
                return False
    return True

# 시간초과

# import re
# def solution(phone_book):
#     for number in phone_book:
#         p = re.compile("^"+number)
#         for num in phone_book:
#             if number != num and p.match(num):
#                 return False
#     return True