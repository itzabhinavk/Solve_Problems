# Day 20 - 100 Days of Code Challenge


# function 

#function is a block of code that is used to perform a specific task. 
# It is a reusable pice of code that call be used multiple times in a program. 
# It helps to break the code into smaller and manageable parts. 
# It also helps to reduce the code redundancy and makes the code more readable and maintainable.


# basic code of function 
def functioneexample(name ):
    print("hey ", name ,"welcome to my coding journey")
    print("this is my first function in python")
    return "function executed successfully"
name = input("Enter your name: ")
result = functioneexample(name)
print(result)




#default argument

def myself(name="abhinav",age=19,location="banka",skills="diploma in computer science and engineering " ):
    print("good morning sir i'm ",name, "from",location,"dirstic", "my last collification is",skills,"and i am ",age,  "years old thank you sir")
    return "thank you sir "

myself(name="varsha",age=18,location="banka")





#calculate the average of number

def average(*number):
    sum=0
    for i in number:
        sum+=i
    print("average of the number is ", sum/len(number))
average(int(input("Enter the number to calculate the average of the number: ")))





def name(**name):
    print("Hello ",name["fname"],name["mname"],name["lname"])

name(mname="abhinav",lname="kumar",fname="james")



# formal and actual argument 
def number(num1,num2):
    num1+=1
    num2+=2 
    print(num1)
    print(num2)

a=int(input("Enter the first value: "))
b=int(input("Enter second number: "))
number(a,b)
print(a)
print(b)

