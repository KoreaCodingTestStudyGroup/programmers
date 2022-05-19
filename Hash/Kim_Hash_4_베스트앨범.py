"""장르 별로 가장 많이 재생된 노래를 두개씩 모아 베스트 앨범을 출시, 노래는 고유번호로 구분
1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
genres 와 노래 재생횟수 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유번호를 순서대로 return 하도록 solution함수를 완성해라"""

"""genres[i]는 고유번호가 i인 노래 장르
plays[i]는 고유번호가 i인 노래가 재생된 횟수
genres 와 plays 길이는 같으며 1~10000
장르 종류는 100개 미만
장르에 속한 곡이 하나 라면, 하나의 곡만 선택 합니다.
모든 장르는 재생된 횟수가 다르다."""


### -------------- 틀린코드-------------
# 리스트를 딕셔너리에 추가했더니 같은종류의 같은 재생횟수를 가진 음악이 추가되지 않았음.
# def solution(genres, plays):
#     answer = []
#     dict = {}
#     dict2 = {}
#
#     for i, j in zip(genres, plays):
#         dict[j] = i
#
#     for i, j in dict.items():
#         dict2[j] = dict2.get(j, 0) + i
#     dict1 = sorted(dict.items(), key=lambda x : (x[1], x[0]), reverse=True)
#     dict2 = sorted(dict2.items(), key=lambda x: x[1], reverse=True)
#     print(f"dict = {dict}")
#     print(f"dict = {dict1}")
#     print(f"dict2 ={dict2}")
#     idx = []
#     for index, (i, j) in enumerate(dict.items()):
#         idx.append([j, i, index])
#
#     idx.sort(key=lambda x: (x[0], x[1]), reverse=True)
#
#     for i, _ in dict2:
#         cnt = 0
#         for x, y, z in idx:
#
#             if i == x:
#                 if cnt == 2:
#                     continue
#                 answer.append(z)
#                 cnt += 1
#     print(idx)
#     return answer


def solution(genres, plays):
    answer = []
    idx = []
    dict = {}
    for index, (i, j) in enumerate(zip(genres, plays)):     # [인덱스, 장르, 재생횟수]의 형태로 list에 삽입
        idx.append([index, i, j])
    for _, i, j in idx:
        dict[i] = dict.get(i, 0) + j    # {장르 : 재생횟수의 합}의 형태로 dict 생성
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)   # 재생횟수를 기준으로 정렬
    idx.sort(key=lambda x : (x[1], x[2]), reverse=True) # 1.장르, 2.재생횟수 두개를 기준으로 정렬
    # [4, 'pop', 2500], [1, 'pop', 600], [5, 'k', 300], [6, 'k', 300], [3, 'classic', 800], [0, 'classic', 500], [2, 'classic', 150]]

    for i, _ in dict:   # 재생횟수를 기준으로 정렬된 dict를 순회
        cnt = 0         # 장르당 2개의 음악만 출력되야하기 때문에 cnt=0 으로 두고 list에 추가될때마다 +1 cnt ==2 라면 추가하지 않고 다음 장르로 넘어감
        for x, y, z in idx: # 리스트에서 인덱스, 장르, 재생횟수 선택

            if i == y:  # 리스트의 장르가 dict의 인덱스와 같다면
                if cnt == 2:
                    continue
                answer.append(x)    # answer list에 index 추가
                cnt += 1
    return answer




genres = ["classic", "pop", "classic", "classic", "pop", "k", "k"]
plays = [500, 600, 150, 800, 2500, 300, 300]
print(solution(genres, plays))
# [4, 1, 3, 0]

