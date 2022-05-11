# clothes의 각 행은 [의상의 이름, 의상의 종류]
# 스파이의 의상 수는 1~30
# 같은 이름을 가진 의상은 존재 X
# clothes의 모든 원소는 문자열로 이루어져 있습니다.
# 모든 문자열의 길이는 1~20 이하인 자연수이고 알파벳 소문자 또는 'ㅡ'로만 이루어져있습니다.
# 스파이는 하루에 최소 한개의 의상은 입는다.

from itertools import product

def solution(clothes):
    answer = 1
    dict = {}
    dict2 = {}
    for i in range(len(clothes)):
        dict[clothes[i][0]] = clothes[i][1] # {의상이름 : 의상종류}의 형태로 dict생성

    for j in dict.values():
        dict2[j] = dict2.get(j, 0) + 1  # {의상종류 : 개수}의 형태로 dict생성

    for i in dict2.values():
        answer *= (i+1) # 각 의상 종류에 대해서 (개수 + 입지 않은 경우)를 곱해준다.
    return answer-1     # 스파이는 최소 한개의 의상을 입기 때문에 아무것도 입지 않은 경우의 수를 빼준다.






clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))