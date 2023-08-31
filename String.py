#string
#It is an alpha numeric, symbols within quotes single or doubles.
#a="ocean"
#a='ocean'
#access
# it can acess through the index position
#index position always start with 0
#index last position always -1
#within square brackets
a="ocean"
##        o  c  e  a  n
##index   0  1  2  3  4
##last    -5 -4 -3 -2 -1
#length   1  2  3  4  5

##print(a[0])
##print(a[-5])
##print(a[-1])
##print("length of the string",len(a))
##
##checking
##membership operator
##print("s" in a)
##userinput=input("enter the character")
##if userinput in a:
##    print("It is present in this string")
##else:
##    print("It is not present in this string")
##
##looping in string:
##for i in a:
##    print(i)
##for i in range(len(a)):
##for i in range(5)
##    print(i,a[i])
##    
##slicing string
##a="ocean academy"
##print(a[2:5])
##print(a[2:])
##print(a[:8])
##print(a[:-1])


##TASK:
##1.print the even position value from the given string
##2.print the  odd position value from the given string
##3.solving the coding bat website problems string 1 heading without using no loop


##Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
##
##
##non_start('Hello', 'There') → 'ellohere'
##non_start('java', 'code') → 'avaode'
##non_start('shotl', 'java') → 'hotlava'

string1=input("enter the string 1")
string2=input("enter the string 2")
if(len(string1)>0 and len(string2)>0):
    print(string1[1:]+string2[1:])
else:
    print("Strings length atleast in")

