#it is a block of code, which only runs when it is called
#defining a function
def demo():
    print("Welcome to Python Class")

#calling a function
demo()

#parameters and arguments
##A parameter is the variable listed inside the parentheses in the function definition.
##
##An argument is the value that is sent to the function when it is called.
#function parameter
def addition(a,b):#paramter
    print(a+b)
#calling
addition(6,7)#Argument

#return a function

def retname(a,b):
    return a*b
print(retname(5,4))
    
