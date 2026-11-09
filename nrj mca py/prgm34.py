s=int(input("Enter the length of the square:"))
area=lambda s: s * s
print(area(s))
  
p=int(input("Enter the length of the rectangle:"))
r=int(input("Enter the breadth of the rectangle:")) 
areaa=lambda p, r:  p * r
print(areaa(p,r))
  
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))  
area=lambda b, h: 0.5 * b * h
print(area(b,h))
