t=int(input())
for _ in range(t):
    l,r,a=map(int,input().split())
    x=r//a
    if(x-1>=a):
        print(x-1)
    else:
        print(r)