def solution(A):
    # write your code in Python 2.7
    
    N = len(A)
    
    if N == 0 or N == 1:
        return 0
    
    min = A[0]
    profit = 0
    
    for i in xrange(1, N):
        if min > A[i]:
            min = A[i]
        if profit < A[i] - min:
            profit = A[i] - min
            
    return profit
