fruits = ['apple', 'banana', 'mango', 'orange', 'grape', 'pineapple', 'papaya', 'guava', 'watermelon', 'kiwi', 'apple', 'banana', 'strawberry', 'blueberry', 'pomegranate', 'mango', 'pear', 'peach', 'cherry', 'litchi']
vegis = ['potato', 'onion', 'tomato', 'carrot', 'cabbage']

fruits.append('coconut')
fruits.insert(0,'papaya')
print(fruits)
fruits.extend(vegis)
print("now fruit has ", fruits)
fruits.remove('potato')
fruits.pop(0) 
print("after removal fruit has ", fruits)
print("carrot position in list",fruits.index("carrot"))
# print("ladyfinger position in list ",fruits.index("ladyfinger"))
print("count of apple ",fruits.count('apple'))
print("count of ladyfinger ",fruits.count('ladyfinger'))
fruits.sort()
print("sorted fruits ",fruits)
fruits.reverse()
print("reversed fruits ",fruits)
fruits.clear()
print("empty fruits list ",fruits)
vegis2 = vegis.copy() # perfect way to copy list into another list
# vegis2 = vegis wrong way
vegis.clear()
print("vegis ",vegis)
print("vegis 2 ",vegis2)