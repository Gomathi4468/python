#set-It is sequence of number separated by comma within curly brackets {}
#mutable
#unchangeable
#unordered
#not allow the duplicates allow
#does not have index position

#add or remove

set1={1,3.4,5,6,3,3}
print(set1)
for i in set1:
    print(i)

#find the length of the list
print(len(set1))

#checking
print(1 in set1)

#add method
set1.add(7)
print(set1)


#update method
set1.update("ddafa")
print(set1)

#remove items
set1.remove(3)
print(set1)
set1.pop()
print(set1)
    
