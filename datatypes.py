#datatypes
###integer
##    Without decimal value. Eg: 123,21,1. keyword:"int"
###floating
##    with decimal value. Eg:12.52. Keyword: "float"
###boolean
##    2 Values True or False. Keyword:"bool"
###String
##    all the alpha numeric , symbols within double quotes or single quotes.
##    Eg: "123" "abc@gmail.com" Keyword:"str"
###list
##    sequence of elements separated by comma within square brackets.
##    Eg: [1,3,4,6] Keyword:"list"
###tuple
##    sequence of elements separated by comma within parenthesis ().
##    Eg:(1,3,4,5) keyword:"tuple"
###set
##    sequence of elements separate by comma within curly brackets {}.
##    Eg: {1,3,45,5} keyword: "set"
###dict
##    sequence of elements both keys and value separated by comma within curly
##    brackets {}. Eg:{"name":"ocean","age":12} keyword: "dict"
##
##a=10
###type()- it is used to check the datatype
##print(type(a))
##b=10.5
##print(type(b))
##c="asdfa3r03a"
##print(type(c))
##a=10
##a=20

#How to get user input in runtime
#syntax:
##variablename=datatype(input("statement"))
##a=10
##a=int(input("Enter the value of a is integer"))
##b=str(input("Enter the value of string"))
##d=input("Enter the value of string")
##c=float(input("Enter the value of floating value"))
##e=bool(input("Enter the value of boolean"))
##print(a)
##print(b)
##print(c)
##print(d)
##print(e)


##o/p
##
##My name is variable and i am variable years old.
name=input("Enter your name")
age=int(input("Enter your Age"))
print("My name is",name,"and i am",age,"years old.")
