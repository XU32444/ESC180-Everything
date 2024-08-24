import copy
L = [[1,2,3], [4,5,6], [7,8,9]]

def f(L):
    L1 = copy.deepcopy(L)
    L1[0] = [2,7,4]
    return print(L1)

f(L)
print(L)