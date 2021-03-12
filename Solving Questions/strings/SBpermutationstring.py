'''
finding all substring of a string that are a permutation of 
another string

'''

a = 'XYYZXZYZXXYZ'
b = 'XYZ'
seenb = {}
for right in range(len(b)):
    if b[right] not in seenb:
        seenb[b[right]] = 1
    else:
        seenb[b[right]] += 1
seena = {}
left = 0
count = 0
for right in range(len(a)):
    if a[right] not in seena:
        seena[a[right]] = 1
    else:
        seena[a[right]] += 1
        
    if right - left + 1 == len(b):
        if seenb == seena:
            count += 1
            print(left)
        seena[a[left]] -= 1
        left += 1
    