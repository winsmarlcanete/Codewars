# Build Tower
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

def tower_builder(n_floors):
    
    counter = 1
    asterisk  = []
    floorlist = []
    newfloorlist = []
    for x in range(1, n_floors+1):
        
        print(counter)

        for j in range(0,counter):
            asterisk.append("*")
        
        counter += 2

        floorlist.append("".join(asterisk))
        asterisk.clear()
    
    whitespacecounter = 0
    whitespace = []
    finalwhitespace = ""

    for x in floorlist[::-1]:

        for j in range(0,whitespacecounter):
            whitespace.append(" ")
        
        finalwhitespace = "".join(whitespace)

        newfloorlist.append(finalwhitespace + x + finalwhitespace)

        whitespacecounter += 1

        whitespace.clear()
        finalwhitespace = ""


    return newfloorlist[::-1]
    
    

print(tower_builder(3))