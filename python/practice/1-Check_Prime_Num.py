num=int(input("enter the any number  "))
i=2
tat=0
while i<num**0.5:
    if num%2==0:
        tat=1
        print("not prime ")
        break
    i+=1
    if tat==0:
        print(num,"number is prime")