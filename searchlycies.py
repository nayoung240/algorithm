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
'''

from collections import defaultdict
from bisect import bisect_left, bisect_right

def count_by_lange(lst, start, end):
    return bisect_right(lst, end) - bisect_left(lst, start)
    
def solution(words, queries):
    answer = []
    
    cands = defaultdict(list)
    reverse_cands = defaultdict(list)
    
    # 길이별 저장
    for word in words:
        cands[len(word)].append(word)
        reverse_cands[len(word)].append(word[::-1])
    
    # 정렬 O(NlogN)
    for cand in cands.values():
        cand.sort()
    for cand in revserse_cands.values():
        cand.sort()
    
    # 탐색 O(N*logM)
    for query in queries:
        # 접두사
        if query[0] == '?':
            lst = reverse_cands[len(query)]
            start, end = query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')
        # 접미사
        else:
            lst = cands[len(query)]
            start, end = query.replace('?', 'a'), query.replace('?', 'z')
        answer.append(count_by_lange(lst, start, end))
        
    return answer
