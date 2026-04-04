line = "The Quick Brown Fox Jumps Over The Lazy Dog"
print("Original string ",line)
print("lower string ",line.lower())
print("upper string ",line.upper())
print("is this string in uppercase ",line.isupper())
print("is this string in lowercase ",line.islower())
print("is this string has only alphabets ",line.isalpha())
print("is this string has only alpha numeric letters ",line.isalnum())
print("is this string has only numbers letters ",line.isnumeric())
print("is this string has only has space ",line.isspace())
print("is this string in title case ",line.istitle())
print("No of letters including space ",len(line))

fruits = ["Apple","Banana","Chikoo","Custard Apple","Dragon Fruit","Grapes","Guava","Jackfruit","Litchi","Mango","Mosambi","Orange","Papaya","Pear","Pineapple","Pomegranate","Strawberry","Watermelon"]

#convert fruit list into string 
connector = " "
words = connector.join(fruits)
print(words)
alphabets = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
print(alphabets)
#convert string into list where each word of string is individual item
letters = alphabets.split()
print(letters)

sentence = "India is known for its culture, India values unity, India drives innovation, India nurtures diversity, and India continues to grow globally."
print("Original sentence",sentence)
print(sentence.replace("India","Bharat"))
print(sentence.replace("India","Bharat",1))
print(sentence.replace("India","Bharat",2))