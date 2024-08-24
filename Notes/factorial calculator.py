#How many trailing zeros are in a factorial?

def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product

def trailing(n):
    count = 0
    while n % 10 == 0:
        n = n / 10
        count = count + 1
    if count == 0:
        print("no trailing zeros")
    return count



if __name__ == '__main__':
    print(trailing(factorial(13)))