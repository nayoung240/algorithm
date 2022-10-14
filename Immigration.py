'''
입국심사를 기다리는 사람 수 n
각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 

문제포인트
- 최댓값은 가장 오래걸리는 심사대에 모든사람이 심사를 받는 것
- input의 최대길이가 지나치게 길고, 특정 값을 찾아야 하는 문제라면 이분탐색을 의심해보자
'''
def solution(n, times):
    start = 1
    end = max(times)*n 
    answer = end
    while start <= end:
        mid = (start + end) // 2

        people = 0
        for time in times:
            people += (mid // time)

        if people < n:
            start = mid+1
        else: #people >= n:
            end = mid-1
            answer = min(answer, mid)

    return answer
