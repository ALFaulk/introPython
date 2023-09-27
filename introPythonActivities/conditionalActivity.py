# 1. What is the difference between 
# a parameter and an argument in a python function

#A parameter is a data holder while an argument is the data.

# 2. In your own words, describe what 
# a conditional statement (if/else) is 

#If/else is a function that depends on if something is true than thats the answer but if its false than else is the answer.

# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )

money_in_game = 900.00
price_of_gameItem = 300.00

if money_in_game > price_of_gameItem:
    print('You have the game item')
else:
    print("sorry, insufficent coins")

# 4. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def food_In_Fridge():
    food_In_Fridge = False

if food_In_Fridge == True:
    print("Time to cook!")
else:print("Time to Shop!")


# 5. Create a function that checks the inventory of cereal for a store. 
# your function should have a parameter that accepts an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

