# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(st):
    
    letters = []
    batch = []
    batch2 = ""
    batch3 = []
    counter = 0
    
    for letter in st.casefold():
        letters.append(letter)
    
    for letter in letters:
        counter += 1
        
        for x in range(0,counter):
            batch.append(letter)
        
        batch2 = "".join(batch)
        batch.clear()
        batch3.append(batch2.capitalize())
        
        
    return "-".join(batch3)

print(accum("abcd"))