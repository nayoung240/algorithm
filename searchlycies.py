'''
실패한 풀이 - 정규식 -> 효율성 실패
출제의도는 트라이 자료구조 or 이분탐색
'''
import re

def solution(words, queries):
    answer = []
    
    for a in queries:
        alen = len(a)
        reg = a.replace('?','[a-z]')
        cnt = 0
        
        for b in words:
            if alen != len(b):
                continue
                
            p = re.compile(reg)
            s = p.match(b)
            # print(s)
            
            if s != None:
                cnt += 1
                
        answer.append(cnt)

    return answer

'''
트라이 구조를 이용한 풀이
'''
class Trie:
    def __init__(self, val, depth=0):
        self.child = {}
        self.num = {}
        self.val = val
        self.depth = depth

    def push(self, word):
        node = self
        while len(word) > 0:
            node.num[len(word)] = node.num.get(len(word), 0) + 1
            if word[0] not in node.child:
                node.child[word[0]] = Trie(word[0], node.depth + 1)
            node = node.child[word[0]]
            word = word[1:]


    def search(self, word):
        node = self
        while len(word) > 0:
            if word[0] == '?':
                return node.num.get(len(word), 0)
            if word[0] not in node.child:
                return 0
            node = node.child[word[0]]
            word = word[1:]

    def __repr__(self):
        return 'num: {}; val: {};'.format(str(self.num), self.val)

def solution(words, queries):
    answer = []
    t1 = Trie('')
    t2 = Trie('')
    for word in words:
        t1.push(word)
        t2.push(word[::-1])

    for query in queries:
        if query[0] != '?':
            val = t1.search(query)
        else:
            val = t2.search(query[::-1])
        answer.append(val)
    return answer

'''
이진탐색 풀이
- bisect_left, bisect_right를 count by range
- 와일드카드 문자는 접두사 아니면 접미사에 있으므로 => 접두사인경우 단어를 뒤집어 저장 
'''
import bisect

# 값이 [left_val, right_val] 데이터의 개수를 반환하는 함수
def count_by_range(a, left_val, right_val):
    right_index = bisect.bisect_right(a, right_val)
    left_index = bisect.bisect_left(a, left_val)
    return right_index - left_index

arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    # 단어의 길이별로 저장, ?가 접미사냐 접두사냐에 따라 저장한다.
    # 접두사인경우 뒤집어서 저장한다.
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])
    
    # 이진 탐색을 위해 각 길이별 단어 리스트를 정렬한다.
    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for x in queries:
        if x[0] != '?':
            # ___a ~ ___z 까지의 단어 갯수를 찾음
            result = count_by_range(arr[len(x)], x.replace('?', 'a'), x.replace('?', 'z'))
        else:
            result = count_by_range(reversed_arr[len(x)], x[::-1].replace('?', 'a'), x[::-1].replace('?', 'z'))

        answer.append(result)

    return answer
