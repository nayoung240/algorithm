N = int(input())
requests = list(map(int, input().split()))
M = int(input())
start, end = 0, max(requests)

while start <= end:  # 이분탐색
    mid = (start + end) // 2  # 상한액 설정
    curr = 0
  
    for i in requests:
        if i >= mid:  # 요청한 금액이 상한액 이상이라면
            curr += mid  # 상한액 더하기
        else:  # 상한액 미만이라면
            curr += i  # 요청한 금액 더하기

    if curr <= M:  # 예산 총액이 총 예산 이하라면
        start = mid + 1
    else:  # 예산 총액이 총 예산을 초과한다면
        end = mid - 1

print(end)
