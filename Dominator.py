# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    counter = []
    
    for i in xrange(N):
        if not counter:
            counter.append((A[i], 1, i))
        elif counter[0][0] == A[i]:
            counter[0] = (counter[0][0], counter[0][1]+1, counter[0][2])
        elif counter[0][1] > 1:
            counter[0] = (counter[0][0], counter[0][1]-1, counter[0][2])
        else:
            counter.pop()
    
    true_count = 0
    if counter:
        for i in xrange(N):
            if A[i] == counter[0][0]:
                true_count += 1
            if true_count > N/2:
                return counter[0][2]

    return -1
