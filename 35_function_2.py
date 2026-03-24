import shutil
import datetime as dt #dt is aliasname for datetime
column = shutil.get_terminal_size().columns
# 1	 Without return value without argument
def printLine():
    global column 
    #it should print 100 astrik 
    print("")    
    letter = "*"
    for count in range(1,column):
        print(letter,end='')
    print("")

# 2	Without return value with argument 
def printCenter(message):
    global column
    print(message.center(column))
# 3	 With return value without argument
def getDate():
    #current date 
    date = dt.datetime.today()
    today = str(date.day) + "/" + str(date.month)  + "/" + str(date.year)
    return today 
# 4	With return value with argument 

printLine()
printCenter("THE EASYLEARN ACADEMY")
printLine()
today = getDate()
print(today)
