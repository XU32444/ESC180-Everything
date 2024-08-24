L = [1,23,4,2,423,23,5,3,2,5,6,7]
list1 = [1,2,3,4,5,6]
list2 = [1,2,3]
def count_evens(L):
    s = 0
    for i in range(len(L)):
        if L[i] % 2 == 0:
            s = s + 1
    return s

lis = [1, 2, 5, 7, 213]

def list_to_str(lis):
    s = ""
    t = ""
    for i in range(len(lis)):
        if i == len(lis) - 1:
            b = lis[i]
            s = s + str(b)
        else:
            b = lis[i]
            s = s + str(b) + ","
    t = "[" + s + "]"
    return t

def lists_are_the_same(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True




def list1_start_with_list2(list1, list2):
    if len(list1) >= len(list2):
        for i in range(len(list2)):
            if list1[i] == list2[i]:
                return True
            else:
                return False
    return False

def match_pattern(list1, list2):
    for i in range(len(list1) - len(list2)):
        chk= False
        for d in range(len(list2)):
            if list1[i + d] != list2[d]:
                chk = True
                break
        if chk == False:
            return True
    return False



list0 = [1,2,3,3,5]

def duplicates(list0):
    for i in range(len(list0)):
        if i < len(list0) - 1:
            if list0[i] == list0[i + 1]:
                return True
    return False


if __name__ == '__main__':
    print(list_to_str(lis))












