# MID TERM QUIZ 


# RULES

# I. You may use google/ W3 schools to assist you with this exam

# II. Please make sure your answers/ responses are readable. You can write your written answers as comments or strings but 
# make sure that you are spacing your answers away from the questions. 

# III. You may use notes in your reposiory

# IV. You may not use any additional computing devices 
# (only one computer should be out).

# V. You may not use your phone during the quiz under any circumstances.
# If it is an emergency please request to be excused from the class. 

# VI. You may not have music or videos playing during the quiz
# under any circumstances. 

# VII. You may not use any LLM / AI applications under any circumstances. 
# Any one caught using  these applications will automatically fail the quiz.

# VIII. Save your work under the QUIZES folder

# _____________________________________________________________________


# Take your time, read the questions thoroughly, look for context clues

# The Code editor is your friend, run/ test your code. The computer will tell you if it's right or wrong.

# GOOD LUCK

# _____________________________________________________________________



# 1. Describe what a computer program is and what does it do. 

"A computer program is a set of instructions that a computer performs. A computer program gives the computer specific instructions to preform."

# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.). 
  
"Complexity is the measurement of the amount of resources it takes to program. An examaple of complexity is typing out the entire link to get to a youtube video."
"Abstraction is the simplification of complex programs. An example of abstraction is just hitting the youtube app button and going to the video instead of typing out the whole link."

# 3. What is Syntax in Python and why is it important to write proper syntax?

"Syntax is the rules that defines how a Python program has to be written."
"It's important to writew proper syntax because it helps the code look structured."

# 4. What is a function, and why do we wrap our code inside of functions?

"A function is a block of code."
"We wrap our code inside of functions so we acn catch any mistakes we make in the coding process."

# 5. Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables. 

"Camal Case is when there is a lower case letter then an uppercase letter, like this camel_Case."
"Pascal Case is when the it starts with an uppercase letter, like this Pascal_Case. "
"Snake Case is when all the letters are lowercase, like this snake_case"
"The three name rules for python are only letters A-Z, numbers 0-9 and _ underscores."

# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student= 'Richard'

print(name)
print(student)

"The output will be the names walter and richard."

# 7. Describe the difference between each of the following assignment operators:
# = 
# ==
# !=
 
"= means that something is equal to the opreator."
"== means that something is true."
"!= means that something is not equal to the opreator."

# 8. What type of data can be stored in a python list?

"Intigers, Booleans, Strings, Floats, etc"

# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse. 

def word():

    word1 = input('Please input the word that you would like to revsere. ')

    print(word1[::-4])
word()



# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively. 
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal. 


def subtracting(x,z):
    print(x - z)

subtracting(6,9)

def adding(x , z):
    print( x + z)

adding(6 , 9)

def multiplying(x,z):
    print(x*z)

multiplying(6,9)

# 11. What is the difference between a function argument and a function parameter. 

"A function argument is the data/information."
"A function parameter is a place holder for data."


# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program. 
# the goal of your program is to check a user's password and make sure it meets the company's password requirements. 
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that 
# their password was created successfully, and if it was not, should send back a message with one of the following issues. 

# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue?

"When you see type error that means that something is in the wrong type."
"I would go to wher the red underline is and check my code so I could correct it."

# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve 
# the issue?

"When you see indent error that means that something was either indented wrong or was not indented at all."

# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying 
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again. 
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth 
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator. 


# 16. Which item is at index 5
giftShopping=['xbox','sneakers','necklace','clothing','laptop','gift card']

"The item at index 5 is laptop"

# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function. 
upToNumber = 30

# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary. 
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise. 
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify. 

# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters. 
# and should evaluate which number is larger. Your function should then print the largest number. 

# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name. 
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items. 
# Once your gift bag hits its limit of six (6) items your program should print a message saying 
# that the gift bag is full and print the list of items in the gift bag.   
 


 