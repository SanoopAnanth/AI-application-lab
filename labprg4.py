#4a set operation
#4b calculator
#4c calander
my_set={1,2,3}
#discard won't raise any error if element is not present
my_set.discard(0)
print(my_set)
#passing another list to update
my_set.update({4})
print(my_set)
#remove operation
my_set.remove(2)
print(my_set)
another_set={1,3,5,6}
#union operation
res=my_set.union(another_set)
print(res)
#intersection operation
res=my_set.intersection(another_set)
print(res)
#pop operation in set
print(my_set.pop())
#add operation
my_set.add(10)
print(my_set)
#clear method
print(my_set.clear())