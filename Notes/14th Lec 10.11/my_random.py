# shotgun debugging
# non-systematically trying to fix

# a = 2193782
# b = 2139213891273
# m =2**32 - 1
# x = 1
# for i in range(10):
#     x = (a*x+b)%m
#     print(x/m)
def initialize():
    import time
    seed(int(time.time()))


def random():
    global x
    a = 1283123
    b = 2138912397
    m = 2**32 - 1

    x = (a*x+b) % m
    return x/m


def seed(seed_x):
    global x
    x = seed_x

initilaize()

# import time
# time.time()# number of seconds since Jan 1, 1970 at midnight
# seed(time.time())
# print(random())
# print(random())


#seed: the starting point of a sequence of pesedo-random numbers
# seed(5)
# print(random())
# print(random())
# print(random())

