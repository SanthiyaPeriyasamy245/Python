 

# set is unordered and not indexed and it removes duplicates

set1={1,2,3,4,5,2,3,1,1,3}
set2={3,4,5,6,7}
print(set1.union(set2)) # it combines both sets
print(set1|set2) # union
print(set1 & set2) # it will give you common between two sets , intersection
print(set1-set2) #difference
print(set1^set2) # symmertric removes common values in set1 and set2
set1.add(10)
print(set1)
print(set1 is (set2)) 
data=set([11,22,33,44,55])
print(data)

