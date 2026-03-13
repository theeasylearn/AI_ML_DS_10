#write a program to find out profit or loss amount from given products purchase and sales price 
purchase_price = int(input("Enter product purchase price"))
sales_price = int(input("Enter product sales price"))
difference = sales_price - purchase_price

if difference>0:
    print(f"you have made profit of {difference}")

if difference<0:
    print(f"you have made loss of {difference}")

print("good bye.")