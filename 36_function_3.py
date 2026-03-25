# write a program to create function getSeconds which return total seconds of given hours,minutes and seconds. *(here minutes and seconds are optional and their default value is 0) 
# input: hour 10 minutes 10 seconds 5 then output 36605
def getSeconds(hours,minutes=0,seconds=0):
    print(f" hours {hours} minutes = {minutes} seconds = {seconds}")
    totalSeconds = (hours * 60 * 60) + (minutes * 60) + seconds
    return totalSeconds


h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))
s = int(input("Enter seconds: "))

totalSeconds = getSeconds(h,m,s)
print(f"total seconds using 3 arguments  {totalSeconds}")

totalSeconds = getSeconds(h,m)
print(f"total seconds using 2 arguments  {totalSeconds}")

totalSeconds = getSeconds(h)
print(f"total seconds using 1 arguments  {totalSeconds}")



