import math

figure = int(input())


def pythagoreantriplets(n):
    for i in range(1, int(n/3)+1):
        for j in range(i+1,int(n/2)+1):
            
            c  = i*i + j*j
            m = n-i-j
            
            if (c==(m*m)) and ((i+j+m==n)):
                print(i*j*m)
            
            
pythagoreantriplets(figure)






