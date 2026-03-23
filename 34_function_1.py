#1st example of functions
def getSquare(number):
    square = number * number
    return square

def getQube(number):
    qube = number * number * number
    return qube 

def getPower(base,exponent): #base = 2, input 5
    power = base 
    for count in range(1,exponent):
        power = power * base #4 
    return power 

num = int(input("Enter number"))
square = getSquare(num) #call function 

qube = getQube(num)

power = getPower(2,6) # 64
print(f"square = {square} qube = {qube} power = {power}")
