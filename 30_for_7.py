#write a program to display all the leap years between 2000 to 2100
for year in range(2000,2101):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"{year:8}",end=' ')
        else:
            print(f"{year:8}",end=' ')