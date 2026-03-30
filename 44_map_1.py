import math
#example of map and lambda function 
numbers = [5, -3, 12, 7, -8, 0, 19, -2, 4, 11, -6, 8, -1, 14, -9, 3, 6, -4, 10, -7]
print("original list ",numbers)

#define lambda using map to convert negative numbers into positive numbers 
positive_numbers = map(lambda num: int(math.fabs(num)),numbers)
print(list(positive_numbers))

list1 = [2, 5, 8, 11, 14, 17, 18, 23, 26, 29]
list2 = [1, 7, 6, 9, 12, 15, 20, 25, 29, 45]

print(list1)
print(list2)
#define lambda using map to that return largest value at each and every position in two list 
list3 = map(lambda num1,num2: num1 if num1>num2 else num2,list1,list2)
print(list(list3))


