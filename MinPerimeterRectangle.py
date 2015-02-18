import math

def solution(N):
    # write your code in Python 2.7
    
    for i in reversed(xrange(1, int(math.sqrt(N))+1)):
        if N % i == 0:
            return (i + N / i) * 2
    
