# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    
    string = ""
    list = []
    
    for x in s:
        list.append(x.capitalize())
        
    string = "".join(list)
    
    return string