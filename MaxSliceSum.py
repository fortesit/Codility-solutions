# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    N = len(A)
    Max = A[0]
    curMax = A[0]
    
    if N == 1:
        return A[0]
    
    if N == 2:
        return max((A[0], A[1], A[0]+A[1]))
    
    allNegative = True
    negativeMax = A[0]
    for i in xrange(N):
        if A[i] > 0:
            allNegative = False
            break
        if negativeMax < A[i]:
            negativeMax = A[i]
    
    if allNegative == True:
        return negativeMax
    
    if curMax < 0:
        curMax = 0
    
    for i in xrange(1, N):
        curMax += A[i]
        if curMax < 0:
            curMax = 0
        if Max < curMax:
            Max = curMax
        print i, curMax, Max

    return Max
    
