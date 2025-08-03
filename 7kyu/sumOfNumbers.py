# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples (a, b) --> output (explanation)
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

def square_digits(num):
    
    strnum = str(num)
    
    list = []
    list2 = []
    
    for x in strnum:
        list.append(int(x)**2)
        
    for j in list:
        
        list2.append(str(j))
    
        
    return "".join(list2)

print(get_sum(0,-1))