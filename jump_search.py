import math
def jump(arr,n,l):
    sq=int(math.sqrt(l))
    for i in range(0,l,sq):
        if arr[i]>=n:
            for j in range(i,0,-1):
                if arr[j]==n:
                    return j
    return -1
arr=list(map(int,input("input elements").split()))
i=1
while(i):
    n=int(input("enter element to search"))
    result=jump(arr,n,len(arr))
    print("element found at",result)
    i=int(input("enter 0 to exit"))