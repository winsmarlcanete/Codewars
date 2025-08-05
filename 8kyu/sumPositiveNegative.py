# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    
    countP = 0
    sumN = 0
    
    
    for x in arr:
        if x > 0:
            countP += 1
        else:
            sumN += x
            
    return [countP, sumN] if len(arr) > 0 else []

