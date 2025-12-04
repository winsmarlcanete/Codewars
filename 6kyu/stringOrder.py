# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(sentence):

    splitted = sentence.split()
    
    splitted2 = splitted.copy()

    for x in splitted:
        
        for j in x :
            
            if j.isdigit():
                splitted2.pop(int(j)-1)
                splitted2.insert(int(j)-1, x)
                print(splitted2)
    
    return " ".join(splitted2)

print(order("4of Fo1r pe6ople g3ood th5e the2"))  