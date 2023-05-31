'''
내가 작성한 코드
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0

        for i in range(len(s)):
            for j in range(1, len(s)+1):
                # 문자열 끝을 초과하면 break
                if i+j >= len(s)+1:
                    break

                word = s[i:i+j]

                # 거꾸로 뒤집어도 동일한가 = 팰린드롬
                if word == word[::-1]:
                    answer += 1

        return answer
     
'''
코드 개선
- 중첩 for문에서 1이 시작이아니라 i로해주면 break 필요 없음
'''
class Solution:
	def countSubstrings(self, s: str) -> int:
		answer = 0

		for i in range(len(s)):
			for j in range(i, len(s)):
				word = s[i:j+1]
        
				if word == word[::-1]:
					answer += 1

		return result
