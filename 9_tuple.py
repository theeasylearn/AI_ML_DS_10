box = ('Car',100,False,True,3.14,None)
beg = ('pen',300)
print(box,beg)
print(box[0]) #Car
print(box[1:3]) #100 & False 
print(box[:3]) #print 1st three item 
print(box[3:]) #all items 3rd item onwards 
print(box+beg)
print(box)
# box[0] = 'Plane' #error
print('good bye')
print("count of car",box.count('Car'))
print("index(position) of 100",box.index(3.14))
