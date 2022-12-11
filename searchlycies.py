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
def make_trie(words, reverse):
    dic = {}
    for word in words:
        dic.setdefault(len(word), {})
        current_dic = dic[len(word)]

        if reverse:
            word = word[::-1]

        for letter in word:
            current_dic.setdefault(letter, [0, {}])
            current_dic[letter][0] += 1
            current_dic = current_dic[letter][1]
            
    return dic

def count(query, new_query, cur_dic):
    if len(query) not in cur_dic.keys():
        return 0

    current_dic = cur_dic[len(query)]
    for letter in new_query:
        if letter not in current_dic.keys():
            return 0

        current_dic = current_dic[letter][1]
        
    return sum([v[0] for k, v in current_dic.items()])
    
def solution(words, queries):
    answer = []
    dic = make_trie(words, False)
    reverse_dic = make_trie(words, True)
    
    for query in queries:
        new_query = query.replace('?', '')
        if query[0] == '?':
            temp = count(query, new_query[::-1], reverse_dic)
            answer.append(temp)
        else:
            temp = count(query, new_query, dic)
            answer.append(temp)
        
    return answer
