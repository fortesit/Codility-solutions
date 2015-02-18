# you can use print for debugging purposes, e.g.
# print "this is a debug message"

import math

def solution(N):
    # write your code in Python 2.7
    
    result = 0
    
    for i in xrange(1, int(math.sqrt(N))+1):
        if i * i < N:
            if N % i == 0:
                result += 2
        if i * i == N:
            result += 1
            
    return result
