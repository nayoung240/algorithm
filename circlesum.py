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
