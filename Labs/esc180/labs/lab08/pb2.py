def binary_search(L, e):
    low = 0
    high = len(L)-1
    times = 0
    while high-low >= 2:
        times += 1
        mid = (low+high)//2 #e.g. 7//2 == 3
        if L[mid] > e:
            high = mid-1
        elif L[mid] < e:
            low = mid+1
        else:
            return mid,times
    if L[low] == e:
        return low,times
    elif L[high] == e:
        return high,times
    else:
        return None

L = [0,1,2,3,4,5,6,7]
print(binary_search(L, 7))


