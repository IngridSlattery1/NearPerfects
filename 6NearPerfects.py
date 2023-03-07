import math

def sigma(n):
    sigma=0
    for i in range (1, int(n/2)+1):
        if n % i == 0:
            sigma += i
            
    sigma += n
    
    return sigma
    
range=input('What do you want your range to be? ')
range=int(range(max))
for n in range (1,range):
    d1=[]
    d2=[]
    count=0
    d1.append(1)
    d2.append(n)
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            d1.append(i)
            d2.append(n/i)
            count+=1
    for j in range (1,count+1):
        for l in range (j+1,count+1): 
            for m in range (l+1, count+1):
                d=d1[j]+d2[j]+d1[l]+d2[l]+d1[m]+d2[m]
                if sigma(n) == 2*n + d:
                    print(n)
                    print(f'({d1[j]},{d2[j]})')
                    print(f'({d1[l]},{d2[l]})')
                    print(f'({d1[m]},{d2[m]})')
