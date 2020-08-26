i=1
print("enter array to search elements")
arr=list(map(int,input().split()))
while(i):
    print("enter element to search")
    n=int(input())
    flag=0
    for i in arr:
        if i==n:
            flag=1
            print("number found")
            break
    if flag==0:
        print("number not found")
    i=int(input("enter 1 to continue else 0"))
print("exited!")
