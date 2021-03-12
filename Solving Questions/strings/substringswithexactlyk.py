# Count number of substrings with exactly k distinct characters


'''
Solution:

For this question,
Brute force would be to get all the substring O(n^2)
            and compare each substring with exactly k distint characters 0(n)

More Efficient way:
Would be to trade space for time
we would have an extra space 0(n) where a list would be used add the strings that complete the criteria and 
a dictionary which helps us know the when each substring has exactly k distint characters

Works by:
having two loops, the inner loop iterates till substring has exactly k distint characters and 
at each time we meet a criteria we add to the result[] and start all over again i+1 from where we started
having an empty dictionary

'''


st = "abcadce"
k = 4
result = []
maxi = 0
for i in range(len(st)):
    chars = {}
    for j in range(i, len(st)):
        if st[j] not in chars:
            chars[st[j]] = 1
        else:
            chars[st[j]] += 1

        if len(chars) == k:
            result.append(st[i: j + 1])
            maxi = max(maxi,len(result))


print(len(result))
print(result)