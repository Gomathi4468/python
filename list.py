#list
#It is sequence of an element is separated by comma within square brackets.
#keyword is list
#it allows a duplicate value
#it is changeable
#it is mutable datatype
list1=[1,2,4,5,6,7,4,5]
print(list1)
#Accessing the list
#access the list using index position
#index position is always start with 0 and ends -1
#within square brackets
print(list1[1])
print(list1[-1])
print(list1[2:5])
#checking the value
#membership operator
b=5
if b in list1:
    print("True")
else:
    print("False")

#change the list items

list1[3]=9
print(list1)
list1[2:5]=[4,5,6]
print(list1)
#add
#insert method
list1.insert(6,10)
print(list1)
#append
list1.append(13)
print(list1)

#remove--value
list1.remove(10)
print(list1)
#pop--index
list1.pop(2)
print(list1)

list1.pop()
print(list1)

#looping in list1
for i in range(len(list1)):
    print(list1[i])
for i in list1:
    print(i)
#clear
list1.clear()
print(list1)
#del
del list1
print(list1)
