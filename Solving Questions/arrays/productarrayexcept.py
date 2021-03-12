# def check_string(string1,string2):
#     if len(string1) != len(string2):
#         return False

#     union_string = string1 * 2
#     print(union_string)
#     b = union_string.find(string2)
#     if b == -1:
#         return False
#     return True, b

# print(check_string('abcde','eabcd'))

def  findnumber(array):
    x  = 0
    for num in array:
        x ^= num
    return x
print(findnumber([1,1,2,2,3]))













