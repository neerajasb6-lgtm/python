n=int(input("Enter a number:"))
t=n
sum=0
while t>0: 
     d=t%10
     sum=sum+d**3
     t=t//10
if sum==n:
     print("Armstrong")
else:
     print("Not Armstrong")        
