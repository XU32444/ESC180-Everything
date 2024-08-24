def simplify(n,m):
    a = []
    for i in range(min(n,m) + 1):
        if m % (i + 1) == 0 and n % (i + 1) == 0:
            a.append(i + 1)
    a.sort()
    b = a[-1]
    #if n % b == 0 and n % a == 0:
    return str(n/b) + "/" + str(m/b)

if __name__ == "__main__":
    print(simplify(1,2))