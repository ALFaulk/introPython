# Save this as pythonReview.py

# In your own words describe, what a computer program is?
# A computer program is a set of instructions on to program various apps or video games. Computer programs can instruct what a character design looks like in a video game, the character movements or move. Computer programs can instruct an app like a caculator to caculate equations that are put into the caculator.

# In your own words, describe what it mean to call a function? 
# To call a function is to rewrite the function by the end of your code, so the code can actually run. For example  if I wrote a function def bike() at the end of the function you would put down bike() again to run the code.

# Create a elevator function that will run specific lines of code 
# based on the conditions provided by a user. If the user types in 101,
# the function should print out they are going to the boys latin office, 
# if they type in 203, they are going to the gym, 
# and if they type in the letter g, the lobby. else, 
# if the input doesnt match any of the values provided, 
# tell the user that floor doesn't exist and to please
# enter a valid floor number.


def elevator():

    print('Hello welcome to the elevator, choose a floor to go to:')
user_floor=input()

if user_floor== 'g':
    print('You are in the lobby')
elif user_floor== '203':
    print('You are at the gym')
elif user_floor== '101':
    print('You are at the boys latin office')
else:
    print('This floor does not exist, please choose another floor')

elevator()


# Create a function that will do the following calculation.
# Your function should take in three argument. it should add the first
# two arguments and then the sum of the first two (2) should be divided 
# by the third argument. You function should then print the result.
