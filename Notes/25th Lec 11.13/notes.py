# 25th Lec notes

#Turing thesis
#Anything that you can do with loops in python, you can do on any computer, vice versa

# Extended Church Turing thesis:
#In python efficiently, you can do on any computer efficiently, and vice versa

def find_i(L,e):
    '''find the index of the element e in list L'''
    return L.index(e)

# How efficient is find_i ?
# In seconds, for a list L of length n, if we dont get lucky, with L[i] == e for small i, how long will the function take?


# In seconds, for a list L of length n, if we dont get lucky, with L[i] == e for e at the end of L, how long will the function take?

# In operations, for a list L of length n, if we dont get lucky, with L[i] == e for e at the end of L, how long will the function take?

# operation: an elementary transformation of the data in the computer

# L = [5, 2, 10]
# e = 10

# L is set, e is set (2 ops)
# compute len(L), store it somewhere (2)
#set up range(k opertaion)

# setting i to 0,1,2 (3 operations)
# figure out if we are done (3 operations)
# comparing L[i] to e, 1 op, (accessing L[i], 1 for comparing L[i] to e, 2*3 ops return i = 1)

#approximately, len(L) * (1 + 1 + 2) + c

# in the wrost case, if e is at the end of L, the runtie will be proporational to the length of L

#dont know how many seconds/
#opreration:

#runtime is s * len(L) * 4 + s * c


def find_i(L,e):
    '''find the index of the element e in list L'''
    for i in range(len(L)):
        if L[i] == e:
            return i

# worst-case asymptotic runtime complexity for an input of size n:

# For an input of size n, for the input that makes most unlucky, what is the runtime proportioanl to

# for find_i: for len(L) = n, the worst case runtime is proportioanl to n (approximately)











