#print multiplication table of given number 

number = int(input("Enter number"))
for multiplier in range(1,11):
    result = number * multiplier #5 
    # 5 x 1 = 5
    print(f"{number} X {multiplier:2} = {result:3}")
