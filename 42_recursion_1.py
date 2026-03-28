#decimal to binary 
def toBinary(number):
    if number>0:
        reminder = number % 2 
        number = number // 2
        toBinary(number)
        print(reminder,end='')
number = int(input("Enter number"))
# number = 8 
toBinary(number)


