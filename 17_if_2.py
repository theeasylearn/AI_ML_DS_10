#write a program to findout whether how many days given month has 
# 1 3 5 7 8 10 12 this month has 31 days 
# 4 6 8 11  this month has 30 days 
# 2 month has 28/29 days 

month = int(input("Enter months "))

if month == 2:
    print("this month is 28/29 days")
    exit() #stop program in between 

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("this month has 31 days")
else:
    print("this month has 30 days")


