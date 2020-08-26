def binary(arr,l,r,n):
    if r>=l:
        mid=l+(r-l)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            binary(arr,l,mid-1,n)
        else:
            binary(arr,mid+1,r,n)
    return -1

print("BINARY SEARCH")
arr=list(map(int,input("enter array elements").split()))
i=1
while(i):
    n=int(input("enter element to search"))
    result=binary(arr,0,len(arr)-1,n)
    print("number found at",result)
    i=int(input("enter 1 to continue else 0"))
print("exit!!!")
