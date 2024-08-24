def power(x,n):
    res =1.0
    for i in range(n):
        res = res * n # float multiplications are constant time
    return res

# O(n): the runtime is linear in n, or proportional to n


def power_rec(x,n):
    if n == 0:
        return 1.0
    else:
        return x * power_rec(x,n-1)


# n + 1 recursive calls, each call takes the same amount of time,
# there fore the runtime is proportional to n + 1
# so proportional to n for very large n
# O(n)

# x^n = (x^(n/2))^2 = ((x^(n/4))^2)^2 = (x^(n/8))^2)^2)^2

# n -> n/2 -> n/4 -> n/8
# ~ log2(n) steps

# x ^ n = (x^(n//2))^2 (*x if n is odd, *1 if n is even)

def power_rec_fast(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x

    half_pwer = power_rec_fast(x,n//2)
    if n%2 == 0:
        return half_pwer ** 2
    else:
        return (half_power**2)*x

# log2(n) calls
# each call takes constant time
# O(log(n)) runtime























