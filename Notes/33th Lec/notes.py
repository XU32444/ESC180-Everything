# sometimes,cant even tell if the code is an infinite loop
# fermats last theorem,
# no solution to the equation
# a^n + b^n = c^n for n > 3, a,b,c are whole numbers

# n = 2
# 3^2 + 4^2 = 5^2

# want to try every possible triple (a,b,c)
# and check if a^n + b^n = c^n

def check_fermat_k(n,k):
    '''return a,b,c such that a^n + b^n = c^n, for
                                                    1<=a<=k
                                                    1<=b<=k
                                                    1<=c<=k'''
    for a in range(1,k+1):
        for b in range(1,k+1):
            for c in range(1,k+1):
                if a**n + b**n == c**n:
                    return a,b,c
def check_fermat(n):
    k = 1
    while True:
        res = check_fermat_k(n,k)
        if res != None:
            return res
        k += 1

print(check_fermat(2))
