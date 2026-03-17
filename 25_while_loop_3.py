#write a program to convert given amount into words 
# input : 12345
# output : one two three four five 

words = ['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
list = []
amount = 12345

while amount>0:
    reminder = amount % 10
    list.insert(0,words[reminder]) # ['five']
    amount = amount // 10

print(''.join(list))
