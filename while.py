#while syntax
##start
##while(condition):
##    statement
##    step

##stop=int(input("enter the range"))
##i=1
##while(i<=10):
##    print(i)
##    i+=1

#Nested while loop

##i=1
##while(i<=5):
##    print("ocean",end=" ")
##    j=1
##    while(j<=5):
##        print("Academy",end=" ")
##        j+=1
##    print()
##    i+=1


#Find the Armstrong Number

num=int(input("enter the number"))
b=str(num)
length=len(b)
originalNumber=num
result=0
##print(b)
##print(length)
while(num!=0):
    rem=num%10
    result+=rem**length
    num//=10
print(result)
if(result==originalNumber):
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")

    
