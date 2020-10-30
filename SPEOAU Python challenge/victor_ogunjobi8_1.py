import itertools


first_input= input() 
second_input= int(input())

addthem = []

for v in itertools.permutations(first_input):
    addthem.append(v)
    addthem.sort()
    


result =''.join(addthem[second_input-1])
print(result)



