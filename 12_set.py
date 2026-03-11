#create set
fruits = {'Cherry','kiwi','mango','pinapple','orange'}
print(fruits)
fruits.add('apple') 
fruits.add('orange') #ignore because there is already orange in set 
print("set after inserted new items ",fruits)
fruits.remove('kiwi')
# fruits.remove('banana') #error 
print("set after removing item",fruits)
vegis = ["potato", "tomato", "onion", "carrot", "cabbage", "potato", "tomato", "spinach", "brinjal", "peas", "carrot", "cucumber", "radish", "onion", "beans", "capsicum", "potato", "pumpkin", "spinach", "tomato"]
print(vegis)

#convert it into set
unique_vegis = set(vegis)
print(unique_vegis)

#convert it back into list
vegis = list(unique_vegis)
print("again displaying vegis ",vegis)

set1 = {1,2,3}
set2 = {3,4,5}

print(set1,set2)

union = set1.union(set2)
print(union)
intersection = set1.intersection(set2)
print(intersection)
difference = set1.difference(set2)
print(difference)