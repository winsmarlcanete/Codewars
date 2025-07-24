import math

def century(year):
    
    if year%100 <= 99 and year%100 >= 1:
        return math.ceil(year/100) 
    
    else:
        return year/100