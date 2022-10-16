'''
어렵다.
DFS로 풀려다가 실패했는데 성공한 풀이 가져옴
'''
def DFS(n, pos, num, number):
    global answer
    if pos > 8:
        return
    if num == number:
        if pos < answer or answer == -1:
            answer=pos
        return

    nn=0
    for i in range(8):
        nn=nn*10+n
        DFS(n, pos+1+i, num+nn, number)
        DFS(n, pos+1+i, num-nn, number)
        DFS(n, pos+1+i, num*nn, number)
        DFS(n, pos+1+i, num/nn, number)

def solution(N, number):    
    DFS(N, 0, 0, number)    
    return answer
