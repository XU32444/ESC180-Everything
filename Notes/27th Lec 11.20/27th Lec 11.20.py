# using dictionaries to store sparse matrix and vectors

# sparce matrix : matrix where most o the entires are 0

M = [[1, 2, 3],
    [4, 5, 6],]
M[1][2] = 6

M = [[0 0 0 0 ...... 0]
    [0 0 0 5 0.......0]]

#instead of storing n * m entries (n rows, m columns,), most of which are 0
#just store the info where the non-0 entries are

M_sparce1 = {(1,2):51,
            (0,0):43}

M_sparce2 = {(1,2):10,
            (0,0):12}

size = (2,10000000)

def print_sparce_matrix(M_sparce,size):
    for row in range(size[0]):
        for column in range(size[1]):
            if (row,column) in M_sparce:
                print(M_sparce[(row,column)],end = "\t")
            else:
                print(0,end = "\t")
        print(" ")

# M_sparce.get((2,2),0)
# M_sparce[(2,2)] if available, otherwise 0


def add_sparce_matrix(M1,M2):
    sum = {}
    for coords in M1:
        sum[coords] = M1[coords] + M2[coords]
    for coords in M2:
        sum[coords] = M1[coords] + M2[coords]



print_sparce_matrix(M_sparce,(2,7))

# word embeddings


       "dog"  " cat"  "quiz"
V1 = [                      ]
V2 = [                       ]

dist_euc(V1,V2) : sqrt(())

#angle between 2 vectors:
cos(theta_v1v2) = v1.v2/squrt(|v1||v2|) # cos law

|v1| = sqrt(v[0] ^ 2 + v[1] ^ 2, ....)

# two vectors are similar if
dist_euc(V1,V2) is small
cos(theta_v1v2) = v1.v2/squrt(|v1||v2|) is large (i.e close to 1)

# 200,00 words
# if you want to store without using sparce matricies
# all the co-occurence memebers
# (200,000) ^ 2 entries


#not do
emb = {}
emb["dog"] = {}
emb["dog"]["homework"] = 200
emb["dog"]["park"] = 500
# not do
for w1 in all_words:
    for w2 in all_words:
        emb[w1][w2] = compute_cooccurence(w1,w2,corpus)

O(n^2)










































