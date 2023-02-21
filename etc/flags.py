def solution(A):
    pick = []
    answer = 0

    if len(A) < 3:
        return 0

    for i in range(len(A)-1):
        # print(i)
        if i > 0 and A[i-1] < A[i] and A[i] > A[i+1]:
            pick.append(i)

        # print(pick)

    if len(pick) < 3 :
        return len(pick)

    # 제일 처음 peak와 끝 peak 사이에 최대한 깃발을 꽂을 수 있는 갯수
    maxflag = int((pick[-1]-pick[0]) ** (1/2)) + 1
    
    # 제일처음 peak에서부터 조건을 비교하면서, count로 체크한 후 flag 수(f)를 return
    print(pick)
    for f in range(maxflag, 2, -1):
        count = 1
        p = pick[0]

        for pe in pick:
            if f <= pe-p:
                count += 1
                p = pe
            
        if count >= f:
            break

    return f
