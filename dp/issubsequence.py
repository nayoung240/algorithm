'''
나의 꿈을 대신 펼친 Amazing 답
try ~ except ValueError 문 작성할 수 도 있구나 를 알게됨.
'''

class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		for i in range (0, len(s)):    
            index = t.find(s[i])
            		
			if index == -1:
				return False

			t = t[index+1:]

		return True
