#control statement
#break
#continue
#pass
i=2
if(i==1):
    pass

for i in range(5):
    if(i==2):
        break
    print(i)


for i in range(5):
    if(i==2):
        continue
    print(i)

i=0
while(i<=5):
    if(i==2):
        break
    print(i)
    i+=1
i=0
while(i<=5):
   
    i+=1

    if(i==2):
        continue
        print(i)


var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('Current variable value :', var)
print("Good bye!")

for letter in 'Python': 
   if letter == 'h':
      break
      print('This is pass block')
   print('Current Letter :', letter)

#prime
num=int(input("enter the number"))
count=0
i=2
if(num==1):
    print("it is not a prime number")
else:
    while(i<=num):
        if(num%i==0):
            count+=1
        i+=1
    if(count==1):
        print("It is prime number")
    else:
        print("It is not a prime number")
    
