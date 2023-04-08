'''
순열
- permutations(): 하나의 리스트에서 모든 조합 계산(순서포함)
조합
- combinations(): 하나의 리스트에서 모든 조합 계산
- product(): 두개 이상의 리스트에서 모든 조합 계산

튜플을 문자열로 변환하기
''.join(튜플)
'''
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer= []
        phone = {'1':[''], '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        if digits:
            arr = [phone[i] for i in digits]
            answer = [''.join(i) for i in list(product(*arr))]

        return answer
