# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

import cProfile

def max_sequence(arr):
    
    maxSum = 0
    
    size = 1
    
    
    while size <= len(arr):
        for x in range(0, len(arr)): 
            if len(arr[x:x+size]) == size:

                if sum(arr[x:x+size]) > maxSum:
                    maxSum = sum(arr[x:x+size])

        size += 1
    
    return maxSum


cProfile.run("max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])")

#My solution passed 3 of the 4 tests. The last tests involve passing of (5000 up to 10000) lengths of an array which my solution takes a while to complete due to the large argument. But it executes neatly if 5000 and below values of array is passed. This is mainly because it iterates each contiguouos sub-array therefore deemd suboptimal. I do not consider this as a good solution since it failed one of the four tests. I just like to incldue this to a commit.