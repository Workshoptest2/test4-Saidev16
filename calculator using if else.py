x=int(input("enter first number"))
y=int(input("enter 2nd number"))
add=x+y
subtract=x-y
mul=x*y
div=x/y
print("enter your choice")
print("1:addition,2:subtraction,multiplication:3,division:4")
ch=int(input())
if(ch==1):
    print(add)
elif(ch==2):
    print(sub)
elif(ch==3):
    print(mul)
elif(ch==4):
    print(div)
else:
    print("invalid output")
    
