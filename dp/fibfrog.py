def solution(A):
    A.append(1)
    target = len(A)
    fib = fibonacci(target)

    dp = {-1: 0}
    for i in range(target):
        if A[i] == 0: continue
        
        temp_result = []

        for jump in fib:
            if jump > i + 1: 
                break

            if i - jump in dp:
                temp_result.append(dp[i - jump] + 1)
        
        if temp_result: dp[i] = min(temp_result)
        
    print(dp)
    return dp.get(target - 1, -1)

def fibonacci(n):
    fib = [1, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])

    return fib

