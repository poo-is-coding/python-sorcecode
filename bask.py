import math as m
f=int(input())
for j in range(0,f+1):
    for i in range(0,j+1):
        print(m.comb(j,i),end=" ")
    print()
