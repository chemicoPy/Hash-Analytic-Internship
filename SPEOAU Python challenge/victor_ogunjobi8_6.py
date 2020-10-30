
first = int(input())
second = int(input())


def amicable(n):
    sumit = 0
    
    for i in range (1,n):
        if n%i == 0:
            sumit = sumit + i
            

    return(sumit)


if amicable(first) == second and amicable(second) == first:
    print('True')

else:
    print('False')
    
    
    
    

