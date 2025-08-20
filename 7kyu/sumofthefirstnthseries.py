# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return "0.00".

# You will only be given Natural Numbers as arguments.

# Examples (Input --> Output)
# n
# 1 --> 1 --> "1.00"
# 2 --> 1 + 1/4 --> "1.25"
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"

def series_sum(n):
    
    list = []
    counter = 1

    for x in range(0, n):
        
        list.append(1/(counter))
        counter += 3
        
        
    return f"{round(sum(list),2):.2f}"


print(series_sum(3))