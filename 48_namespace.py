balance = 1000
def updateBalance(amount):
    global balance 
    balance = balance + amount 

while True:
    print("Press 1 to check balance ")
    print("Press 2 to deposit amount")
    print("Press 3 to withdraw amount")
    print("Press 0 to exit amount")
    choice = int(input("Enter your choice"))
    if choice == 1:
        print("your balance is ",balance)
    elif choice == 2:
        amount = int(input("Enter deposit amount"))
        updateBalance(amount)
    elif choice == 3:
        amount = int(input("Enter withdraw amount"))
        amount = 0 - amount 
        updateBalance(amount)
    elif choice == 0:
        print("Good bye.")
        break #stop loop
    else:
        print("invalid choice")    
print("end of program")
