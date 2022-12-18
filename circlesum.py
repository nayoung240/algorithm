def solution(elements):
    el_len = len(elements)
    res = set()

    for i in range(el_len):
        ssum = elements[i]
        res.add(ssum)
        
        for j in range(i+1, i+el_len):
            ssum += elements[j%el_len]
            res.add(ssum)
            
    return len(res)

'''
두배로 늘림
'''
def solution(elements):
    result = set()
    
    elementLen = len(elements)
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2
    
    for i in range(elementLen):
        for j in range(elementLen):
            result.add(sum(elements[j:j+i+1]))
    return len(result)
