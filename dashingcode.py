st="3143141592653589793238462643383279"
arr="3,159,314,314314,49,9001,15926535897,14,9323,8462643383279,4,793"
li=arr.split(',')
s=0
j=0
f=list()
while(j<len(st)):
    for i in li:
        if i[0]==st[j]  and len(i)>s and i in st:
            s=len(i)
            l=i
            if(j>=len(st)):
                break;
    s=0;
    f.append(l)
    j+=len(l)
print(len(f)-1,"("+" ".join(f)+")")