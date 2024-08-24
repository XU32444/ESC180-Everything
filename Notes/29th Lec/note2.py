# Bogo sort

#start with a list
# if itis sorted, we are dne
#if its not swap two elements, check if its sorted now

import random

def is_sorted(L):
    for i in range(0,len(L) - 1):
        if L[i+1] < L[i]:
            return False
    return True

def rand_int():
    return int(n*random.random())

def bogo_sort(L):
    while True:
        if is_sorted(L):
            return
        i,j = rand_int(len(L)),rand_int(len(L))
        L[i],L[j] = L[j],L[i]

# in the worst case,the runtime is infinite, because in the worst case, i and j are always the same, even though they are random
#Assuming "reasonably" random i,j
# we are going cycle



# sort last names
L = ["Adsk","Zsasdf","Asdjfh","Hasdsad"]
sorted(L) # O(n log n), n = len(L)



{"A":["Adsk","Asdasd"]
 "Z":["Asasd"], ...}
#Bucket sort
def BucketSort():
    buckets = {}
    for e in L:
        if e[0] not in buckets:
            buckets[e[0]] = [e]
        else:
            buckets[]e[0].append(e)
    all_keys = sorted(buckets.keys())
    res = []
    for k in all_keys:
        res.extend(sorted(buckets[k]))

# worst case complexity?
# in the worst case, everything starts with "A
# complexity: O(n log n), n = len(L)

# if all buckets are small, sorted() might take less time








