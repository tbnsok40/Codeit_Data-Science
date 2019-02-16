def rec(k):
    #base case
    if k <= 0:
        return

    #recursive case
    else:
        print('SSUP')
        k = k-1
        rec(k)
#### at least one base case needed

rec(4)

####
def recu(j):
    if j <= 0:
        return 0
    else:
        return j + recu(j - 1)
print(recu(4))

#### factorial
def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(5))


#### fibonacci
def fib(m):
    if m < 2:
        return m
    else:
        return fib(m-1) + fib(m-2)
print(fib(5))

#### gcd 최소공배수
def gcd(m,n):
    if n>m:
        temp = n
        n = m
        m = temp
        return gcd(m,n)
    else:
        if m % n ==0:
            return n
        else:
            return gcd(m, m%n)
print(gcd(8,2))
print(gcd(9,4))

#### All of this algorithm is the Recursion