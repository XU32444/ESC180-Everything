# -2 2 5 10 20
# L.sort() # Modify the contents of L
# L1 = sorted(L)

def bubble_sort(L):
    for i in range(len(L)):
        swapped = False
        for i in range(len(L)-1-j):
            if L[i+1] > L[i]:
                L[i],L[i+1] = L[i+1],L[i]
                swapped = True
            if not swapped:
                return

# How many times does the innermost block of coed got repeated?

#(len(L)-1) + (len(L)-2) ...... (len(L)-len(L))
# 1 + 2 + 3 + ... + (len(L) - 1) =
    # (sub k = len(L) - 1)

# = len(L)*(len(L)-1)/2 = 0.5(len(L)^2) - 0.5len(L)
# O(len(L) ^ 2)

# counting sort: O(len(L) + max(L))
# bubble sort: O(len(L)^2)
# Merge sort: O(len(L)log(len(L))) # Python's sort
