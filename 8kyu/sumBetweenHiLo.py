# Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6

def sum_array(arr):
    
    if arr == None or len(arr) == 0 or len(arr) == 1:
        return 0
    if len(arr) >= 2:
        arr.sort()
        arr.pop(0)
        arr.pop(len(arr)-1)
        return sum(arr)
    
    else: 0



print(sum_array([1,2,2,3]))
