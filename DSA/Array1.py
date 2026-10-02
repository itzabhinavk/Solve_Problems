# find the target sum in the array 
def target_sum(arr,n,target):
    left=0
    right=n-1
    while (left<right):
        current_sum=arr[left]+arr[right]
        if current_sum==target:
            return left,right
        elif current_sum<target:
            left+=1
        else:right-=1

call_function=target_sum([1,2,3,4,5,6],6,7)
print(call_function)
