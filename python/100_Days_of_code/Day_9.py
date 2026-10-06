# Day 9 - 100 Days of Code Challenge
# Yeh file aapki daily coding journey ka hissa hai.
# Motivation: Aaj ka mehnat kal ki confidence hai.
# Chhoti chhoti steps bhi bade sapne banati hain.

# typecasting in python

a="abhinav"
a1=12
a2="72"
a3=7.4
a4=8
print("type of ",a,"is",type(a))
print("type of ",a1,"is",type(a1))
print("type of ",a2,"is",type(a2))
print("type of ",a3,"is",type(a3))
print("type of ",a4,"is",type(a4))


# print(a1+a2) error throw
print(a+str(a1))   #explicit typecasting
print(a1+int(a2))   #explicit typecasting
print(a3+a4)         #implicit typecasting
print(str(a1)+a2)
print(str(a3)+str(a4))
print("type of ",a,"is",type(a))
print("type of ",a1,"is",type(str(a1)))
print("type of ",a2,"is",type(int(a2)))
print("type of ",a3,"is",type(int(a3)))
print("type of ",a4,"is",type(a4))
