'''
Find the maximum sequence of continuous 1’s formed by replacing at-most `k` zeroes by ones
'''


arr = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
k = 0
zero = 0
left = 0
maxcount = -1

for right in range(len(arr)):
    if arr[right] == 0:
        zero += 1
        
    while zero > k:
        if arr[left] == 0:
            left += 1
            zero -= 1
        else:
            left += 1
    
    if right-left + 1 > maxcount:
        maxcount = right-left + 1