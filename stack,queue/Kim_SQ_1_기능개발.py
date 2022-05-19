import sys
input = sys.stdin.readline


def solution(progresses, speeds):
    answer = []
    result = []
    for index, (i, j) in enumerate(zip(progresses, speeds)):
        cnt = 0
        while i < 100:
            i += j
            cnt += 1
            if i >= 100:
                answer.append(cnt)
                break




    return answer



progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))
