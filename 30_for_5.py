#write a program to count vowels in given string using for loop
line = input("What is your name?")
count = 0
vowels = 'aeiou'
for letter in line:
    if letter in vowels:
        count+=1

print(count)