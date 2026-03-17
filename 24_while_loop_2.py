# example of while loop 
# 1 -4  9  -16 25 -36 49 -64 ..... 400 

number = 1

while number<=20:
    square = number * number
    if number%2==0: #1
        square = 0 - square
    print(square,end= ' ')
    number = number + 1




