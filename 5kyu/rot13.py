# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.


def rot13(message):
    
    stack = []
    
    
    alphaListLower = 97-122 #for reference in unicode
    
    alphaListUpper = 65-90 #for reference in unicode
    
    for x in message:
    
        if x.isalpha() and x.isupper():
            alphapos = (ord(x)-64)+13
            
            if alphapos > 26:
                stack.append(chr((alphapos-26)+64)) 
                
            else:
                stack.append(chr(alphapos+64)) 
            
        elif x.isalpha() and x.islower():
            
            alphapos = (ord(x)-96)+13
            
            if alphapos > 26:
                stack.append(chr((alphapos-26)+96)) 
                
            else:
                stack.append(chr(alphapos+96))
        else:
            stack.append(x)
            
    return ''.join(stack)
        