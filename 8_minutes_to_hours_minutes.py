# write a program to calculate and display hours and remaining minutes of given minutes 
# minutes : 150 output 2 hours and 30 minutes 
# minutes : 75 output 1 hours and  15 minutes 
minutes = input("Enter total minutes")
#convert it into integer
minutes = int(minutes) # 150
hours = minutes // 60 # 2
minutes = minutes % 60 # 30 
print(f"hours = {hours} and minutes = {minutes}")
# print("hours = ",hours,"and minutes = ",minutes)
