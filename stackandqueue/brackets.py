'''
성능: O(N)
예외케이스: '{{{{', '}{'
'''
def solution(S):
    st = []

    for s in S:
        if s == ')':
            if not st or st.pop() != '(':
                return 0
            else:
                continue
        elif s == '}':
            if not st or st.pop() != '{':
                return 0
            else:
                continue
        elif s == ']':
            if not st or st.pop() != '[':
                return 0
            else:
                continue
        
        st.append(s)

    return 0 if st else 1
