def fuse():
    L=[["CIV",92], ["180",98], ["103",99], ["194",95]]
    s = []
    for i in range(len(L)):
        s.append(L[i][1])
    return s

if __name__ == '__main__':
    print(fuse())