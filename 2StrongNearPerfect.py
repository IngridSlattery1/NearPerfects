
range=input('What do you want your range to be? ')
range=int(range(max))
for n in range(1,range):
        extra=sigma(n,1)-2*n
        rootn=int(math.sqrt(n))
        if extra > 2*rootn -1:
            for d in range(1,1+int(math.sqrt(n))):
                if (n %d)==0:
                    if ((n//d) != d) and ((d +(n//d)) == extra):
                        print(n, d, n//d)
    print("All done")    
    
