# Longest substring without repeating characters


'''
Solutions:
Brute force solution would be to get all the substrings in the string O(n^2) and
process the string to get the longest substring without repeating characters i.e O(n)



Efficient solution:
We would have trade a space for time

using a set and a pointer, we would iterate the string  and when we meet a repeating 
character(i.e character in the set), we remove the leftmost character and increment it
until we're not able to see the repeating character. After that we add the current 
character and continue with the iteration and 
at every point we'd get the maxi len by getting the max btw the maxi and the length
of the string calculated by (right-left + 1)
'''

s = "findlongestsubstring"
maxi = 0
seen = set()
left = 0
for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    maxi = max(right-left+1,maxi)
    print(s[left:right+1])


print('Longest substring without repeating character:',maxi)