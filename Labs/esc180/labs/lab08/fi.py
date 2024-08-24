L = open("test.txt", encoding="latin-1").read().split()
dict = {}

words = list(set(L))  #words is like a clean list
for i in range(len(words)):
    dict[words[i]] = 0
for i in range(len(words)): # going through each independent word
    counter = 0
    for e in range(len(L)):
        if L[e] == words[i]:
            counter = counter + 1
    dict.update({words[i]:counter})
def top10(L):
    L1 = L
    L1.sort()
    list = []
    for i in range(10):
        list.append(L1[-1 - i])
    return list
print(top10(L))
##
keylist = []
numberlist = []
for i in dict:
    keylist.append(i)
for i in dict:
    numberlist.append(dict[i])

tops = top10(numberlist)

inverteddict = {}
for e in range(len(keylist)):
    dict.update({numberlist[e]: keylist[e]})
ans = []
for s in range(10):
    ans.append(dict[tops[s]])