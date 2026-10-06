# # Day 7 - 100 Days of Code Challenge



# #alt+shift+dawnArrow 
# #operators in python 
# a=10
# b=96
# sum=a+b
# sub=a-b
# mul=a*b
# div=a/b
# mod=a%b
# expnent=a**6
# floor_div=a//b
# print("addtion of ",a, " and " ,b , " is: ",sum)
# print("substraction of ",a, " and " ,b , " is: ",sub)
# print("multiplication of ",a, " and " ,b , " is: ",mul)
# print("division of ",a, " and " ,b , " is: ",div)
# print("modulus of ",a, " and " ,b , " is: ",mod)
# print("exponent of ",a, " and  2 is: ",expnent)
# print("floor devision of ",a, " and " ,b , " is: ",floor_div)

# print(a==b)
# print(a<=b)
# print(a>=b)
# print(a>b)
# print(a<b)
# print(a!=b)


#check enter name is girl or boy

name= input("Enter your name: ").lower()
i=["i","a","l","m","u"]
print(i*2)
found=False #flag variable
for i in i:
    if i== name[-1]:
        found=True
        break   
if found==True: 
    print("girl ")
else:
    print("boy")
