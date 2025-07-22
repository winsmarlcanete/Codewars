#Write a function which calculates the average of the numbers in a given array.
#Note: Empty arrays should return 0.

def find_average(numbers):
    if len(numbers) != 0: 
        return (sum(numbers)) / len(numbers)
    return 0



