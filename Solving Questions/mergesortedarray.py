nums1 = [1,2,3]
nums2 = [2,5,6]

m = len(nums1)
n = len(nums2)
first = m - 1
second = n - 1
while m > 0 and n > 0:
    if second < 0:
        break
    if nums1[first] > nums2[second]:
        nums1[m+n-1]  = nums1[first]
        first -= 1
    else:
        nums1[m+n-1] = nums2[second]
        second -= 1
print(nums1)