dict1={"name":"vidhya","age":23,"place":"Pondy"}
dict2=dict1.copy()#copy method
print(dict2)
dict3=dict(dict1)
print(dict3)
dict4=dict1
print(dict4)

#user input

dict1={}
len=int(input("enter the length of the dictionary"))
for i in range(len):
    keysvalue=input("enter the keys value")
    dict1[keysvalue]=input("enter the values")
print(dict1)


list1=['b','b','a','b','c','a','e']
dict1={}
for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)

string="ocean"
list1=[]
for i in string:
    list1.append(i)
print(list1)
