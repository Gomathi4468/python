##tuple1=(1,2,3,4,5)
##-->Immutable Type
##-->Value cannot be change
##-->duplicates are allowed
##-->ordered sequence
#Access the tuple throughh index position
#index position start with 0
#last index position -1
tuple1=(1,2,3,4,5,4)
#length the tuple
print(len(tuple1))
print(tuple1[0])
print(tuple1[0:4])
#looping
#both index and value
for i in range(len(tuple1)):
    print(i,"index position",tuple1[i])
#only value
for i in tuple1:
    print("value of",i)

#checking
#membership operator
print(2 in tuple1)
print(2 not in tuple1)
#method
print(tuple1.count(2))
#list conversation
list1=list(tuple1)
print(list1)
tuple2=tuple(list1)
a=tuple1.index(5)
print(a)
#del tuple1  v            
