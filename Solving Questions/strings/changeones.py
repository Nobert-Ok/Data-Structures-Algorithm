# Given a binary array, find the index of 0 to be replaced with 1 to get a maximum length sequence of continuous ones.

'''
Given [0, 0, 1, 0, 1, 1, 1, 0, 1, 1] the index to be replaced is 7 to get a 
continuous sequence of length 6 containing all 1’s.
'''


arr = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1,0]

zero = 0
left = 0
prev = -1
max_count = -1
for right in range(len(arr)):
    if arr[right] == 0:
        zero += 1
        prev = right
        
    while zero == 2:
        if arr[left] == 0:
            left += 1
            zero = 1
        else:
            left += 1
        
    if right - left + 1 > max_count:
            max_count = right - left + 1
            max_index = prev
    

