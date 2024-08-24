#binary search

# if the list L is sorted,
# you can implement a much faster find_i:

# L = [1, 10, 50, 100, 150, 200, 500, 900]
# e = 500

# e = 150
# e = 1

#Binary search
def binary_search():
    '''return the index of e in a sorted list L, assume e is in L'''
    low = 0
    high = len(L) - 1
    # i s.t. L[i] == e is between low and high
    while high - low > 1:
        mid = (low + high) // 2
        if L[mid] == e:
            return mid
        elif L[mid] < e:
            low = mid + 1
        else:
            high = mid - 1
        # high-low is either 1 or 0
        if L[low] == e:
            return low
        if L[high] == e:
            return high
        return None


# 20 questions:

# N possible concepts:
# The most efficient yes/no questions
# Leaves you with -N/2 possibilities either way
# The next question should leave you with N/4 possibilies.


N
N/2
N/4
....
N/2^20 possibilities
There are 2 ^ 20 concepts at most that are possible.































