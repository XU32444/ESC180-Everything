
def power_rec_fast(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n%2 == 0:
        return power_rec_fast(x,n//2) * power_rec_fast(x,n//2)
    else:
        return power_rec_fast(x,n//2) * power_rec_fast(x,n//2) * x

# sum of geometric series
# r^0 + r^1 + r^2 + .. + r^m = (1-r^(m+1))/(1-r)



2^m = 2^(m-1) + 2^(m-1)

def power2(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return power2(n-1) + power(n-1)



