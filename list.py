# Creating a list using python
a = [1,3,4,67,8]

# print the list using print() function
#print(a)

#Access using index using a[0], a[1], a[2]
a[0] = 95
#print(a)

# we can create using different type of data types
C = [2, "Anku", 9.4, True]
#print(C)

# List slicing 
friends = ["Anuj", "Aryan", "Mohit", "Divya",45]
#print(friends[0:4])
#print(friends[-4:])

# List Methods
l1 = [1,4,6,78,45]
#l1.sort()
#l1.reverse()
#l1.append(48) # adds 48 at the end of the list
#l1.insert(4,789) #insters 789 at index 4

l1.pop(2)
#l1.remove(45)
print(l1)