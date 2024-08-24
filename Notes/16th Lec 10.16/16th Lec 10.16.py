#nested loop

#compute(efficiently) the number of trailing zeros in n! (n factorial)

# n! = 1 * 2 * 3* 4 * .... *n
#    = (2 * 5 * 2 * 5) * (...)
#    = (5 ^ k) *(...)
# what is k?

# m = n!

# 1 * 2 * .... * 10 * ... * 15 * ... * 20 *... * 25
# n//5

# n//5 + (n//5) // 5 + ((n//5) // 5) // 5

# 5^1 *

def trailing_zeros():
    res = 0
    cur = n // 5
    res = res + cur
    while cur > 0:
        cur = cur // 5
        res = res +cur
    return res

#Intervire Challenge Question:
#A list contain all integers 1,2,3,..,n except k
#in some order
#find k efficiently
#[5,3,1,4] --->the missing k is 2

def missing_k(L):
    #len(L) if L contains 1..n except
    #for one element n - 1
    #len(L) = n - 1
    #n = len(L) + 1
    n = len(L) + 1
    #try every possible guess
    #about the answer
    for k in range(1, n + 1):
        if k not in L:
            return K
    #return None
























