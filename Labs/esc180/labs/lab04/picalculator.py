def calculator():
    sum = 0
    for i in range(1000):
        rep = (((-1) ** i)/(2 * i + 1))
        sum = sum + rep
    return sum

def calc():
    res = 0
    for n in range(501): # the last number to be added in should be 500
        res = res + n
    return res * 4

def picalc(n):
    minused  = 0
    plused = 0
    for i in range(n):
        minused = minused - (1 / (3 + (4 * i)))
    for i in range(n):
        plused = plused + (1 / (5 + (i * 4 )))
    return 4 * (1 + plused + minused)



if __name__ == "__main__":
    print(picalc(1))