# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    
    N = len(A)
    counter = []
    leader = -1
    leader_count = 0
    left_leader_count = 0
    equi_count = 0
    
    for i in xrange(N):
        if not counter:
            counter.append((A[i], 1))
        elif counter[0][0] == A[i]:
            counter[0] = (counter[0][0], counter[0][1]+1)
        elif counter[0][1] > 1:
            counter[0] = (counter[0][0], counter[0][1]-1)
        else:
            counter.pop()
    
    if counter:
        for i in xrange(N):
            if A[i] == counter[0][0]:
                leader_count += 1
        if leader_count > N/2:
            leader = counter[0][0]
        else:
            return 0
    else:
        return 0
    
    for i in xrange(N):
        if leader == A[i]:
            left_leader_count += 1
        if left_leader_count > (i+1)/2:
            if leader_count - left_leader_count > (N-(i+1))/2:
                equi_count += 1

    return equi_count
