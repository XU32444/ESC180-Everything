# Merge Sort

# 5, 2, 10, 2, 100,        2, 12, 45, 10
# 2, 2, 5, 10, 100         2, 10, 12, 45 '
# 2, 2, 2, 5, 10, 10, 12, 45, 100

# Merge Sort basically
#
# def Merge_sort(L):
#     merge(MergeSort(L[:len(L)//2]))
#
#
#

def merge_sort_slow(L1,L2):
    return sorted(L1 + L2)

def merge(L1,L2):
    res = []
    L1_loc = 0
    L2_loc = 0
    while L1_loc<len(L1) and L2_loc<len(L2)
        if L1[L1_loc] < L1[L2_loc]:
            res.append(L1[L1_loc])
            L1_loc += 1
        else:
            res.append(L2[L2_loc])
            L2_loc += 1
        # at most len(L1) + len(L2)-1 iterations
    res.extend(L1[L1_loc:])
    res.extend(L2[L2_loc:])
    # in the worst case, create a list of length less than len(L1) +len(L2)
    # merge is O(len(L1) + len(L2))
def merge_sort(L):
    if len(L) == 1:
        return L[:]
    return (merge(merge_sort(L[:len(L)//2])),merge_sort(len(L)//2:))


# John von Neumann
# Divide and conquer: solve the problem for parts of the input and then combine the solutions to form the solution to the original problem.







