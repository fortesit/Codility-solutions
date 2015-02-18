#!/usr/bin/env python

input = [1, -2, 3, 10, -4, 7, 2, -5]
part_sum = 0
max = 0

for i in range(len(input)):
    if input[i] + part_sum > 0:
        part_sum += input[i]
        if part_sum > max:
            max = part_sum
    else:
        part_sum = 0

print max