#Pi calculator

import random

def getpi(n):
    s = 0
    for i in range(n):
        x, y = random.random(),random.random()
        if x**2 + y**2 <= 1:
            s = s + 1
        else:
            s = s
    return 4 * s / n

if __name__ == '__main__':
    print(getpi(1000000))

