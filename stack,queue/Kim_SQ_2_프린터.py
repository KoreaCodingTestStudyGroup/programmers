"""
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
"""

def solution(p, l):
    answer = []
    a = []
    for i, j in enumerate(p):
        a.append([i, j])



    while a:
        pr = a.pop(0)
        if any(pr[1] < i[1] for i in a):
            a.append(pr)
        else:
            answer.append(pr)

    for i in answer:
        if i[0] == l:
            return answer.index(i) + 1


# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
