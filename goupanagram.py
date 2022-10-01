'''
Anagram: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것

실패한 내 풀이 (타임오버 발생으로 실패 발생)

Counter 비교하여 같은 글자에서 배열만 바꾼지 체크했다.
ex) abc -> {a:1,b:1,c:1}
if Counter(A) == Counter(B):
'''
from collections import Counter
from collections import deque
import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        dq = deque(strs)
        
        while dq:
            tmp = []
            n = dq.popleft()
            tmp.append(n)
            ncnt = Counter(list(n))
            
            for j in copy.deepcopy(dq):
                jcnt = Counter(list(j))
                
                if ncnt == jcnt:
                    tmp.append(j)
                    dq.remove(j)

             answer.append(tmp)
            
         return answer

'''
좋은 풀이

1. 핵심은 sorted 정렬
- sort(): 리턴 값이 None이며, mutable 하다.
- sorted(): 정렬된 새로운 리스트가 반환되며, immutable 하다.
2. defaultdict로 key:list 형태의 dictionary에 담아두기
-> 키 존재 여부를 체크하지 않을 수 있게 한다.
'''
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list) 
        
        for word in strs: 
            anagrams[''.join(sorted(word))].append(word) 
        
        return list(anagrams.values())
                
                
                
            
    
    
            
