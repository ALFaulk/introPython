# Define While 
# loops are a function that use the while keyword
# we need to give it instructions, like any other function
# keeps a program running so long as its true

i=0
while i <5:
    print('we are learning abt loops')
    i+=1
print('out loop is done')


# break

def breakEx():
    i=0
    while i <100:
        print('we are learning abt loops')
        i+=1
        if i == 5:
            break


# continue skips the condition specified in your program

def continueExample():
    i=0
    while i <= 8:
        i+=1
        if i==5:
            print('skip the number 5.')
            continue
        print(i)
    continueExample()