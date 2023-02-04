'''
실패
처음에 풀고 케이스에 맞게 예외처리를 덕지덕지 붙였지만 결국 마지막 보스 large_max 케이스는 해결할 수 없었다.
'''
def solution(H):
    h_len = len(H)
    end_H = [0] * h_len
    target = 0
    answer = 0
    increasing_h = [i+1 for i in range(h_len)]
    
    # 케이스) boundary_cases
    if len(set(H)) == 1:
        return 1

    # 케이스) large_increasing_decreasing 
    if H == increasing_h or list(reversed(H)) == increasing_h:
        return h_len

    # 케이스) large_piramid
    if H[0] == H[-1]:
        mid = h_len // 2

        if H[0:mid] == list(reversed(H[h_len-mid:])):
            return mid if h_len % 2 == 0 else mid + 1

    while H != end_H:
        for h in range(h_len):
            # pass 조건
            if H[h] == 0:
                target = 0 # 초기화
                continue

            if target > 0:
                if target > H[h]:
                    target = H[h]
                    answer += 1
                elif target < H[h]:
                    diff = H[h] - target
                    H[h] = diff
                    continue
            else:
                target = H[h]
                answer += 1

            H[h] = 0 # pass

        target = 0 # 초기화


    return answer

'''
스택으로 간결하게 푼 정답
시간복잡도: O(N)
'''
def solution(H):
    block_cnt = 0
    stack_arr = []

    
    for i in range(len(H)):
        while len(stack_arr) > 0 and stack_arr[-1] > H[i]:
            stack_arr.pop()

        if len(stack_arr) == 0 or stack_arr[-1] < H[i]:
            block_cnt += 1
            stack_arr.append(H[i])
            
    return block_cnt
