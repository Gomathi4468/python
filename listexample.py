list1=[1,2,3,4]
list3=list1
list4=[]
for x in list1:
    if x%2==0:
        list4.append(x)
print(list4)

#listcomprehension:
list5=[x for x in list1 if x%2==0]
print(list5)

#Sorting lists
a=[2,5,3,2,4,6,69]
a.sort()
print(a)
a.reverse()
print(a)

user input
list1=[]
length=int(input("enter the range"))
for x in range(length):
    a=int(input("enter the value"))
    list1.append(a)
print(list1)
