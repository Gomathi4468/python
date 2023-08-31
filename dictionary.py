#dictionary:
#sequence of element both key and value separated by comma within curly brackets
#keyword:dict
##eg:dict1={"name":"annu","age":20}
#mutable type
###changeable, ordered and does not allow duplicates value
dict1={"name":"ajay","age":20,"place":"pondy"}
print(dict1)
#change the values
dict1['age']=21
print(dict1)
#length
print(len(dict1))
#update #adding
dict1['list1']=[1,3,54,6]
print(dict1)

#Access the dictionary items
print(dict1['name'])
print(dict1['list1'][0])
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1.get('name'))
#update method
dict1.update({'dob':'12:03:1995'})
print(dict1)
#remove
dict1.pop('age')
print(dict1)
dict1.popitem()
print(dict1)
del dict1['place']
print(dict1)
#clear
dict1.clear()
print(dict1)

#delete
del dict1

#looping
dict1={"name":"ajay","age":20,"place":"pondy"}
for x in dict1:#keys
    print(x)
for x in dict1.keys():#keys
    print(x)

for x in dict1.values():#values
    print(x)

for x  in dict1:
    print(dict1[x])

for x in dict1.items():
    print(x)
for x,y in dict1.items():
    print(y)
