from math import isqrt
def Prime_Factorisation(n: int):
    pf = []
    for i in range(2,isqrt(n)+1):
        while n % i == 0:
            pf.append(i)
            n //= i

    if n > 1:
        pf.append(n)

    return pf

print(Prime_Factorisation(114))

N = int(1e5+7)
isPrime = [True]*N
hp = [0]*N
lp = [0]*N

isPrime[0] = isPrime[1] = False
for i in range(2,N):
    if isPrime[i]:
        hp[i] = lp[i] = i
        for j in range(i*i,N,i):
            hp[j] = i
            isPrime[j] = False
            if lp[j] == 0:
                lp[j] = i


def prime_factors(n):
    pf = []
    fact = lp[n]
    while n > 1:
        pf.append(fact)
        n //= fact
        fact = lp[n]

    return pf

divisors = [[] for _ in range(20)]
for i in range(2,20):
    for j in range(i,20,i):
        divisors[j].append(i)


print(isPrime[30])
print(hp[30],lp[30])
print(prime_factors(36))
print(divisors[18])