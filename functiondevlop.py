'''
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 
각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.
'''
import math
import collections

def solution(progresses, speeds):
    maxx = []
    b = []
    answer = []

    for i, prog in enumerate(progresses):
        remainDay = math.ceil((100 - prog) / speeds[i])

        if i > 0:            
            if maxx[-1] < remainDay:
                maxx.pop()
                maxx.append(remainDay)
                b.append(remainDay)
            else:
                b.append(maxx[-1])
        else:
            maxx.append(remainDay)
            b.append(remainDay)

    for val in sorted(collections.Counter(b).items()):
        answer.append(val[1])

    return answer # return [q[1] for q in sorted(collections.Counter(b).items())]

'''
zip(*iterable): 여러 그룹의 데이터를 루프를 한 번만 돌면서 병렬 처리 가능
math.ceil(number): 소수점 아래 올림 (int형)
'''
def solution(progresses, speeds):
    maxx = []

    for p, s in zip(progresses, speeds):
        remainDay = math.ceil((100 - p) / s)

        if len(maxx) == 0 or maxx[-1][0] < remainDay:
            maxx.append([remainDay, 1])
        else:
            maxx[-1][1] += 1

    return [q[1] for q in maxx]

