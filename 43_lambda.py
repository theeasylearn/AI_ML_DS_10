#lambda function to get square
getSquare = lambda number: number * number 
#lambda function to get qube
getQube = lambda number: getSquare(number) * number

#create lambda function that use decision making statement if else 
getMax = lambda num1,num2: num1 if num1>num2 else num2 

num = int(input("Enter any one number"))
square = getSquare(num) #lambda function 
print(square)

qube = getQube(num) #call lambda function 
print(qube)

print(getMax(10,20)) #20
print(getMax(110,50)) #110