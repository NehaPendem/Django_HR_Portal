a=[0.6, 0.7, 0.8, 1.2, 0.4]
n=len(a)
	    
c=0
A=[]
B=[]
C=[]
	    
	    
for i in a:
	       
    if(float(i)>0 and float(i) <2/3):
	        A.append(i)
	            
    elif(float(i)>=2/3 and float(i)<=2):
	        B.append(i)
    elif(float(i)>1 and float(i)<2):
	        C.append(i)
	           
	           
for i in A:
	       i=float(i)
	       
for i in B:
	       i=float(i)
	       
for i in C:
	       i=float(i)
	           
A.sort(reverse=True)
	   #case1 aaa
if(len(A)>=3):
            s=A[0]+A[1]+A[2]
	   
            if(s>0 and s<2/3):
                c+=1
                        
	   #case2 aab
	   
s=A[0]+A[1]
	   
for i in B:
	       if(float(i)>(1-s) and float(i)<(2-s)):
	           c+=1
	           
	   #case3 aac
	   
A.sort()
	   
s=A[0]+A[1]
	   
C.sort()
if(len(C)!=0):
    s+=C[0]
	   
if(s>1 and s<2):
	       c+=1
	       
	   #case4 abb
	   
B.sort()
	   
s=B[0]+B[1]
	   
for i in A:
	       if(i<2-s):
	           c+=1
	           
	   #case5 abc
	   
A.sort()
B.sort()
C.sort()
if(len(C)!=0):
    s=A[0]+B[0]+C[0]
	   
if(s>1 and s<2):
	       c+=1
	       
print(c)
	       
