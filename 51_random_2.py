import random as rd 
countries = ["India","United States","Canada","Australia","Germany","France","Italy","Spain","Brazil","Mexico","China","Japan","South Korea","Russia","United Kingdom","Netherlands","Sweden","Norway","South Africa","Argentina"]

print("complete list ",countries)

print("one random country from list",rd.choice(countries))
print("one another random country from list",rd.choice(countries))
print("one more random country from list",rd.choice(countries))

print("any 2 random countries from list ",rd.choices(countries,k=2))
print("any 3 random countries from list ",rd.choices(countries,k=3))

rd.shuffle(countries)
print(" list after shuffle ",countries)

fruits = ["Apple","Banana","Chikoo","Custard Apple","Dragon Fruit","Grapes","Guava","Jackfruit","Litchi","Mango","Mosambi","Orange","Papaya","Pear","Pineapple","Pomegranate","Strawberry","Watermelon"]
print(fruits) 
print(rd.sample(fruits,k=len(fruits))) 
print(fruits) 

