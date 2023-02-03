'''
테스트케이스가 부족해서 알아왔다.
{  new int [] { 4, 3, 2, 1, 5 }, new int [] { 1, 0, 1, 0, 1 },  3 },
{  new int [] { 4, 3, 2, 0, 5 }, new int [] { 0, 1, 0, 0, 0 },  2 },
{  new int [] { 4, 3, 2, 1, 5 }, new int [] { 0, 1, 0, 0, 0 },  2 },
{  new int [] { 4, 3, 2, 1, 5 }, new int [] { 0, 1, 1, 0, 0 },  2 },
{  new int [] { 4, 3, 2, 5, 6 }, new int [] { 1, 0, 1, 0, 1 },  2 },
{  new int [] { 7, 4, 3, 2, 5, 6 }, new int [] { 0, 1, 1, 1, 0, 1 },  3 },
{  new int [] { 3, 4, 2, 1, 5 }, new int [] { 1, 0, 0, 0, 0 },  4 },
{  new int [] { 3 }, new int [] { 1 },  1 },
{  new int [] { 3 }, new int [] { 0 },  1 },
      
시간복잡도: O(N)
'''

def solution(A, B):
    fishes = len(A)
    st = []

    for i in range(fishes):
        if B[i] == 1:
            st.append(A[i])
        else:
            if st:
                for f in range(len(st)-1, -1, -1):
                    fishes -= 1

                    if st[f] < A[i]:
                        st.pop()
                    else:
                        break

    return fishes
