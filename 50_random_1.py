import random as rd 
#here rd is alias of random 
#random between 0 and 1.0
print(rd.random(),rd.random(),int(rd.random()*100))
#float random number between 10 and 99 
number = rd.uniform(10,99)
print(number)
print(f"round off upto 2 digit {number:.2f}")
#int random number between 10 and 99 
print(rd.randint(10,99),rd.randint(10,99),rd.randint(10,99))
print("random number in range of 10,100 divisible by 10 ",rd.randrange(10,100,10))