# 1. Provided below is some starter code. 
# Fix this code to create a loop that will iterate
# until it gets to the number 10.

# hint: remember there are 3 parts to a loop. 
i=0
while i <= 10:# insert missing code.
    print(i)
    print(i==i)# insert missing code here
    i+=1
# 2. Create a simple while loop that will iterate over a the following condition:
# The loop will ask the user to enter the secret number. The secret number is 3. 
# If the user enters the secret number correctly, the loop will stop and tell the user
# the can win a prize. 
# If the user puts in an incorrect secret number, the loop will ask them to enter the 
# correct secret number. 

user_number= input('what is the code? ')

while 'something' == '3':
    print(' not correct! please enter the correct password')
    user_number= input('what is the code')

print('correct! Here is your prize.')


# 3. describe the difference between a while loop and a conditional statement. 
# Try be as specific as you can

"The while loop we can execute a set of statements as long as the condition is true and the"
"conditional statement uses the signs < > <= >="

# 4. Create a while loop that will iterate over the list of names 
# and print out only the following name: William

names= ['Avery','Paige','William','Ade','Jasmyn','Crystal']

x = len(names)
print(x)

i=0
while i < 2: 

    i+=1
print(names[i])

# BONUS QUESTION
# Describe the differences between a FOR loop and WHILE loop. 