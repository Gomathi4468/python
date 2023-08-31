#default arguments
#positional arguments
#Keyword arguments(named arguments)

#Positional arguments

def add(a,b):
    return a+b
print(add(3,2))

#Keyword arguments

def add(a,b):
    return a+b
print(add(b=4,a=3))

#default arguments

def add(a,b,c=10):
    print(a+b+c)
add(c=9,a=10,b=5)

#arbitary arguments
def add(*a):
    #print(a[0])
    for i in a:
        print(i)
add(43,45,67)

#arbitary keyword arguments

def add(**a):
    for i in a:
        print(i)
        print(a[i]) 
        
add(name="jayakrishnan",age=20) 
