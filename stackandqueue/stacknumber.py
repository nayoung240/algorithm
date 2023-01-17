'''
문제 이해가 좀 어려웠다.

입력
첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

출력
입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
'''

n = int(input())
result = []
stack = []
count = 1
tmp = True
# n = 8
# ex = [4,3,6,8,7,5,2,1]

for i in range(n):
    num = int(input())
    # num = ex[i]
    
    while count <= num:
        stack.append(count)        
        result.append('+')
        count+=1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        tmp = False
        break
        
if tmp == False:
    print("NO")
else:
    for i in result:
        print(i)
