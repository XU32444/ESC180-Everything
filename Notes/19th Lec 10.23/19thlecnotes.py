# 19th Lecture

# aliasing
# two varables refering to the same address

L1 = [1, 2, 3]
L2 = L1
L1[0] = 2
# now L2[0] = 2

L2 = L1.copy() # 2072     |    [@1064,@1064,@1096]
#create


#variable table
#
#  name   |   address
#  L1     |   @2024
#  L2     |   @2072
L2[0] = 3 #L1[0] is not affected
L3 = [L1,L2]
L4 = L3.copy #shallow copy
L5 = []
for e in L3:
    L5.append(e) #same as L4 = L3.copy shallow copy, a new


L4[0][0] = 1 # L3[0][0] is now also
L4[1] = 3 # L3 not affected
#L1 and L4 are not aliases
# but L3[0] and L4[0] are aliases
# changing the contents of L3[0] = changing the contents of L4[0]
# BUT changing L3[0] to something else is not the same as changing L4[0]


#

# memory table
#
# address  |  value
# 1032     |    1
# 1064     |    2
# 1096     |    3
# 2024     |    [@1032,@1064,@1096]
# 2072     |    [@1064,@1064,@1096]
# 3004     |    [@2024,@2072]
# 3036     |    [@2024,@2072]



def f(L):
    pass
    # L and L1 are aliases
    #as if you said, local L = L1

if __name__ == "__main__":
    L1 = [5, 6, 7]
    f(L1)














































