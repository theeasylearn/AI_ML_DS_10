import math 
number = float(input("enter float value"))
print("original value",number)
print(f"ceil value of {number} ",math.ceil(number)) 
print(f"floor value of {number} ",math.floor(number)) 
print(f" truncated value {number} ",math.trunc(number)) 
print(f" float and integer part of {number}")
print(math.modf(number))

number2 = int(input("any positive/negative number"))
print(f"Original negative number {number2} and now in positive ",math.copysign(number2,1))
print(f"Original negative number {number2} and now in negative ",math.copysign(number2,-1))
print(f" absolute value of {number2} ",math.fabs(number2))
number2 = int(math.fabs(number2))
print(f"factorial of {number2} ",math.factorial(number2))
print(f"reminder of 10 %3 ",math.fmod(10,3))

