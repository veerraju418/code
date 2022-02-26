n=int(input())
l=list(map(int,input().split()))

res=[]
for dig in l:
    dig=str(dig)
    even=0
    for i in dig:
        if int(i)%2==0:
            even+=int(i)
    res.append(even)
print(*res)
