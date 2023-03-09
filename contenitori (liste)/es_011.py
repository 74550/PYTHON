from operator import length_hint


x=[0,1,2,3,4,5,6,7,8,9,10]
x1=x[0:length_hint(x)//2]
x2=x[length_hint(x)//2:]
print(x1)
print(x2)
x1.append(5)
print(x1)