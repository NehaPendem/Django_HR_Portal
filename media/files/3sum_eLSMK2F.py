import sys
def threeSumClosest(a, k):
        n=len(a)
        
        a.sort()
        l=[]
        
        p1=0
        p2=0
        s=sys.maxsize
        for i in range(n):
            
            p1=i+1
            p2=n-1
            
            while(p1<=n and p2>=i+1 and p1!=p2):
                
                
                
            
                if(a[p2]+a[p1]<=k-a[i]):
                    p1+=1
                else:
                    
                    p2-=1

                if(p2==n or p1==i or p1==n or p2==i):
                    break
                
                
                print(p1,p2,i)
                if(abs(s-k)>=abs(a[p2]+a[p1]+a[i]-k) and p1!=p2):
                    print('hi')
                    
                    s=a[p2]+a[p1]+a[i]
                    
                
                
                

        return s 
a=[ -10, -10, -10 ]
k=-5

print(threeSumClosest(a,k))
