def f(a):
    l=[]
    n=len(a)

    p1=0
    p2=0

    while(p1<n and p2<n):
        if(a[p1]!=1 and a[p2]!=1):
            p1+=1
            p2+=1
        elif(a[p2]==1):
            p2+=1

        elif(a[p2]!=1):
            l.append(p2-p1)
            p1=p2


    print(p1,p2)
    return l



print(f([1,1,1,0,0]))
            
