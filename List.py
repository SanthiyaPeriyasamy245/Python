
# list is mutable
# elements inside the []
# any type of data can be inserted
list=[[7,8],"word",6876,1,2,3,4,6,7,8,9]
print(list)
print(list[-1]) 
print(list[0][1])
print(list[1:])
list.remove("word") # removing data
print(list.pop(5)) #remove the data at particular index when we haven't passed the index it will remove last element.
list[2:2]=[] # empty list at specific range
print(list)
print(list[2:5])
data=[1,2,2,3,3,3,3,4,5,1]
print(data.count(3))
data.sort()
print(data)
data.append(10) # adding element at the append
data.extend([12,45,100])  # adding more than one elements at the end
data.insert(5,50)
print(data)
del data # to delete a list
