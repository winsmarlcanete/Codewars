
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    
    
    list = []
    list2 = []
    
    for x in a1:
        list.append(x)
        
    for x in a2:
        list.append(x)

    for x in list:
        if list2.count(x) == 0:
            list2.append(x)
    
    list2.sort()
    
    return "".join(list2)
