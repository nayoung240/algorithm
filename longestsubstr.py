'''
실패 풀이
-> 이중포문으로는 타임아웃된다. -> 한번의 포문으로 해결해야해!
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        answer = 0

        for i in range(s_len):
            for j in range(i+1, s_len+1):
                breaker = False
                word = s[i:j]

                s_dict = collections.Counter(word)

                for key in s_dict:
                    if s_dict[key] > 1:
                        breaker = True
                        break
                
                if breaker:
                    break
                else:
                    answer = max(answer, len(word))

        return answer
      
'''
어떤이의 정답 - 투포인터로 푼다.
- 문자의 마지막위치를 seen에 저장해둔다. dictionary로
- 이미 나왔던 문자면 l의 시작점을 변경하다.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        length = 0

        for r in range(len(s)):
            char = s[r]

            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
                
            seen[char] = r

        return length


