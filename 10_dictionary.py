#example of dictionary
book = {'name':"mastering python",'price':1500,'author':'Ankit Patel','weight':550.25,'isDigital':False}
print(book)
print(book['name']) #mastering python
#update key's value to python bible
book['name'] = "Python Bible" 
print(book['name'])

#add new key value pair 
book['pages'] = 1000 
print(book)

#remove key and its value
del book['weight']
print(book)