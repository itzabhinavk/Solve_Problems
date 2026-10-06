import os
from random import randint
u_pwd =  input("Enter a passward: ")
pwd = ['a','b','c','e','f','g', '1','2','3','4','5','6']

pw=""
while (pw != u_pwd):
    pw =""
    for latter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,len(pwd)-1)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking passward...")
        os.system('cls')

print("your passward is: "+pw)
     