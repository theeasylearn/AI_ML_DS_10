#concept of keyword arguments 
def getMerit(*arguments):
    '''
        Its values are unpacked into individual variables
        Each variable gets one value in order
        Important rules
        Number of variables must match number of values
        Order matters
        Works with tuple, list, etc.
    '''
    maths, science, english, history, drawing, computer = arguments
    print(f"maths = {maths}, science = {science}, english = {english}, history = {history}, drawing = {drawing}, computer = {computer}")
    total = maths + science + english 
    average = total / 3
    maximum = max(arguments)
    minimum = min(arguments)
    return total,average,maximum,minimum
m = int(input("Enter marks for Maths: "))
s = int(input("Enter marks for Science: "))
e = int(input("Enter marks for English: "))
h = int(input("Enter marks for History: "))
d = int(input("Enter marks for Drawing: "))
c = int(input("Enter marks for Computer: "))
# print(getMerit(m,s,e,h,d,c))
total, average, maximum, minimum = getMerit(m,s,e,h,d,c)
print(total,average,maximum,minimum)
