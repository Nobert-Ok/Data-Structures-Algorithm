def min_number(lst):
    min1 = lst[0] 
    for i in range(len(lst)): 
        # If the other element is min than first element 
        if lst[i] < min1:  
            min1 = lst[i]
    return min1
lst = [5,1,4]
print(min_number(lst))