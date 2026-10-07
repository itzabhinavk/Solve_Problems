#insert of element of an array

def insert(arr,n,item,pos):
    for i in range(0,n-1):
        print(arr[i],end=" ")
        i+=1
    for i in range(n-1,pos-1,-1):
        arr[i+1]=arr[i]
        i-=1
        
    arr[pos-1]=item
    for i in range(0,n):
        print(arr[i])
call_function=insert([1,2,3,4,5,6],7,10,3)