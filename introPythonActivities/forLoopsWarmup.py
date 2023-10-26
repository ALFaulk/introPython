# 1. In your own words, describe what a for loop is?

' A for loop is used to iterate over a sequence'

# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 



# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']

for firstLetter in names:
    if firstLetter[0] == "R":
        print(firstLetter)