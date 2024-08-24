def gcd(n, m):
    a = []
    for i in range(min(n,m) + 1):
        if m % (i + 1) == 0 and n % (i + 1) == 0:
            a.append(i + 1)
    a.sort()
    print(a[-1])
if __name__ == '__main__':
    gcd(66,77)

