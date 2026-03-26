# Arbitrary Argument functions
def sum(*numbers):
    total = 0 
    for num in numbers:
        total=total+num 
    return total 

print("sum of values ",sum(10))
print("sum of values ",sum(10,20))
print("sum of values ",sum(10,20,30))
print("sum of values ",sum(10,20,30,60))
print("sum of values ",sum(10,20,30,60,120))
