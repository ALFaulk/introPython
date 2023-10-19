# Create while loops for the following conditions

# 1. Create a security camera program that uses a while loop to detect if there is an
# object in site. 

def security_camera_people():
    people_On_Camera = 0
    while people_On_Camera < 1 :
        
   
        people_On_Camera +=1
    if people_On_Camera>=1:
        print('Person detected on camera!')
security_camera_people()


# 2. Create a Printer Loop program that will continue to print copies of a document based on the number
# that the user inputs. 

i = 0
copy= (input('how many copys would you like to print'))
what= input('what would you like to print??')
while i < copy:
    print(what)
    i+=1 

# 3. Create a Stop Light Loop that will change the light color based on different time intervals. 
# every 30 seconds the light should change between green and red. 


# 3. BONUS: add an additional condition that will change the light to yellow for 5 seconds before the
# next light change. 