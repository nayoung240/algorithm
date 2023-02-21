def solution(A, B):
  num = 1
  
  if len(A) == 0 or len(B) == 0:
    return 0
  
  if len(A) == 1:
    return 1
  
  endpoint = B[0]
  
  for i in range(1, len(A)):
    if endpoint < A[i]:
      num += 1
      endpoint = B[i]
      
  return num
