#it is module file 
def getSquare(number):
    result = number * number #here square is local variable
    return result

def getQube(number):
    result = getSquare(number) * number #here also result is local variable
    return result

#runnable code(code outside function) this will run automatically whenever we import module
print("Math module is loaded...")