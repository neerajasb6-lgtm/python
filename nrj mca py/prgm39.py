for n in range(1000,10000):
    r=int(n**0.5)
    if r*r==n:
       s=str(n)
       if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
          print(n)
          
