def sum():
    res = 0
    for n in range(1000):
        temp = (((-1) ** n)/(2 * n + 1))
        res = res + temp
    return res

if __name__ == '__main__':
    print(sum())