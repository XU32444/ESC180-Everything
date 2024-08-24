import math

def picalc(n):
    minused  = 0
    plused = 0
    for i in range(n):
        minused = minused - (1 / (3 + (4 * i)))
    for i in range(n):
        plused = plused + (1 / (5 + (i * 4 )))
    return 4 * (1 + plused + minused)

def n_needed(sig_fig):
    counter = 0
    while int(math.pi * (10 ** sig_fig)) != int(picalc(counter)*10**sig_fig):
        counter = counter + 1
    return counter


if __name__ == "__main__":
    print(n_needed(5))
