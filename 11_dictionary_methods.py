#method in dictionary 
details = ['name','surname','gender','age','weight']
print(details)
#create dictionary 
kailash = dict.fromkeys(details) 
print(kailash)
kailash.update({'name':'kailash','surname':'prajapati','age':21,'gender':True,'pincode':364001})
print(kailash)
ankit = dict.fromkeys(details) 
ankit['name'] = "ankit"
ankit['age'] = 42 
ankit['gender'] = True
print(ankit)
# ankit2 = ankit #must not use = sign to copy dictionary, list
ankit2 = ankit.copy()
ankit2.clear()

print(ankit,ankit2)
#print only keys 
print(ankit.keys())

#print only values 
print(ankit.values())

#print dictionary as object
print(ankit.items())

kailash.pop("surname")

#remove last key value pair 
kailash.popitem()
print("after removing multiple ",kailash)

print("your name",kailash['name'])
#below method give key error when key does not exists
# print("your name ",kailash['surname'])

#solution for this problem use get method
print("your name ",kailash.get("surname"))
print("your name ",kailash.get("surname","not found"))



