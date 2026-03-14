#write a program to figure out which person is heaviest person from 3 person weight given by user
weight1 = float(input("Enter 1st person weight"))
weight2 = float(input("Enter 2nd person weight"))
weight3 = float(input("Enter 3rd person weight"))

if weight1>weight2: #outer if 
    if weight1>weight3: #inner if 
        print("1st person is heaviest person")
    else:
        print("3rd person is heaviest person")
else:
    if weight2>weight3: #inner if 
        print("2nd person is the heaviest person")
    else:
        print("3rd person is the heaviest person")

print("End of program")