# Find the highest sum of sub array size k in an array of size n
def max_sum(arr,n,w):
    maxx=-float('inf')
    for i in range(n-w+1):
        current=0
        for j in range(i,i+w):
            current+=arr[j]
        maxx=max(current,maxx)
    return maxx
call_function=max_sum([1,2,3,4,5,6],6,3)
print(call_function)

