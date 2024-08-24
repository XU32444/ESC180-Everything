L=[["CIV",92], ["180",98], ["103",99], ["194",95]]
def look_up(L,num):
    coursename = ''
    counter = 0
    for i in range(len(L)):
        #if counter < len(L):
            if L[i][1] == num:
                coursename = L[i][0]
            else:
                pass
        #counter = counter + 1

    if coursename == '':
        return None
    else:
        return coursename

if __name__ == '__main__':
    print(look_up(L,99))