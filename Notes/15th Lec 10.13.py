#for convention, indicies are i, j ....
for i in range(5, 10, 2):
    print(i)

L = ["hi", 7, 10]
for _ in L:
    print(_)

for i in range(len(L)):
    print(L[i])

i = 0
while i < len(L):
    print(L[i])
    i = i + 1