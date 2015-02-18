#!/usr/bin/env python

def solution(K, L, M, N, P, Q, R, S):
    
    x1, y1, x2, y2, x3, y3, x4, y4 = K, L, M, N, P, Q, R, S
    area = 0
    
    sortedX = sorted([x1, x2, x3, x4])
    sortedY = sorted([y1, y2, y3, y4])
    
    for i in xrange(3):
        for j in xrange(3):
            if (((x1 <= sortedX[i] and sortedX[i] <= x2) and (y1 <= sortedY[j] and sortedY[j] <= y2)) and ((x1 <= sortedX[i+1] and sortedX[i+1] <= x2) and (y1 <= sortedY[j+1] and sortedY[j+1] <= y2)) or ((x3 <= sortedX[i] and sortedX[i] <= x4) and (y3 <= sortedY[j] and sortedY[j] <= y4)) and ((x3 <= sortedX[i+1] and sortedX[i+1] <= x4) and (y3 <= sortedY[j+1] and sortedY[j+1] <= y4))):
                area += (sortedX[i+1] - sortedX[i]) * (sortedY[j+1] - sortedY[j])
                if area > 2147483647:
                    return -1
    
    return area

print area(3,1,6,4,4,0,5,9) # 15
print area(0,0,7,8,4,5,5,6) # 56
print area(0,0,2,3,1,1,4,7) # 22
print area(-5,-7,4,6,-2,0,3,9) # 132
print area(-6,-2,0,6,-2,-6,6,0) # 92
print area(1,1,2,2,3,1,4,4) # 4
print area(1,1,2,2,2,2,3,3) # 2
print area(1,1,2,2,3,3,4,4) # 2
print area(1,1,1,1,1,1,1,1) # 0
print area(-1,-1,-1,-1,2,2,2,2) #0
