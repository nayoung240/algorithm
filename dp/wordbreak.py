'''
DP 점화식 풀이
- 그외 풀이 방법: 메모이제이션, 트라이 자료구조 
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        dp = [i==0 for i in range(n+1)] # [True, False, False,...]

        for i in range(1, n+1):
            # i만큼 돈다.
            for j in range(i):
                # [0 True] -> c -> 
                # ca -> a -> 
                # cat -> [3 True] -> 
                # cats -> [4 True]-> 
                # catsa -> atsa -> tsa -> sa -> a ...
                
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
      
'''
BFS 풀이
'''

from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        seen = set() 

        while q:
            s = q.popleft()
            
            for word in wordDict:
                # 비교대상과 앞자리가 같으면 ex) cats 와 catsandog
                if s.startswith(word):
                    # 뒤를 잘라서 set에 담는다 ex) andog
                    new_s = s[len(word):]
                    
                    if new_s == "": 
                        return True

                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)

                print(word,s,q,seen)
        return False
