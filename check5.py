from math import sqrt

def sigma(n):
  sigma=0
  for i in range (1, int(n/2)+1):
    if n % i == 0:
      sigma += i
  sigma += n
  return sigma

def isPowerOfTwo(n):
    if (n == 0 or n == 1):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True
def checkPrime(n):
  prime_flag = 0
  if (n == 1):
    return False
  if (n == 2):
    return True
  if(n > 2):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i == 0):
            prime_flag = 1
            break
        prime_flag = 0

    if (prime_flag == 0):
      return True
    else:
      return False
    
def isSquare(x):
  sq_root = int(sqrt(n))
  return (sq_root*sq_root) == n

def nearperfect2finder(x):
    for n in range (1,x+1):
        sig = sigma(n)
        maxcheck = sig - 2*n
        if maxcheck>1:
            for d in range (1, int(maxcheck/2)):
                if (n%d==0):
                    if ((maxcheck-d)>0 and n%(maxcheck-d)==0 and (maxcheck-d)!=d):
                        d2 = maxcheck-d
                        d2new = d2
                        dnew = d
                        if (isPowerOfTwo(d) and isPowerOfTwo(d2)):
                          break
                        if (isPowerOfTwo(d)):
                          while (d2new % 2 == 0 and d2new > 2):
                            d2new = d2new/2
                          if (isSquare(d2new)):
                            d2new=sqrt(d2new)
                            if checkPrime(d2new):
                              nNew = n
                              while (nNew % 2 == 0):
                                nNew = nNew/2
                              if checkPrime(nNew):
                                print(n,sig,d,d2)

                        elif (isPowerOfTwo(d2)):
                          while (dnew % 2 == 0):
                            dnew = dnew/2
                            if (isSquare(dnew)):
                              dnew=sqrt(dnew)
                              if checkPrime(dnew):
                                nNew = n
                                while (nNew % 2 == 0):
                                  nNew = nNew/2
                                if checkPrime(nNew):
                                  print(n,sig,d,d2)
    print("all done")
nearperfect2finder(10000)
