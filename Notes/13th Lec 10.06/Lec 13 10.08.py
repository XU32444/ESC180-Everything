#list
L = ["ESC180","PHY180","Track One",3.2123213]
L[0]
L[1]
L[-1]#The last element
L[-2]#the second last element


#the index in python is 0 based
#the first element in a list element number 0
#second element in a list is element number 1

len(L)#the number of elements in the list
print(len(L))#it will return four
L[len(L)- 1]#get the last element = L[-1]
L.append("123a")#add more stuff to the list
"PHY180" in L #check if something is in the list
"PHY180" not in L
L.insert(1,"new")
L.insert(len(L),"new2")#same as append
print(L)
#L. ... what ever after. is called method
a = 4
a + 5
#list methods and functions
#


#examples
marks = [12, 98, 97, 50]
#want to compute average
#plan: add up all the marks and divide the number of elements in mars
for i in range(len(marks)):
    sum = sum + marks[i]
average  = sum / len(marks)
print(average)



#if we want only one element of the list at a time, its better to avoid using i
marks_sum = 0
for mark in marks:
    mark_sum = mark_sum + mark
print("My average is ", marks_sum/ len(marks))


def manual_index(L,e):
    '''Return the location of the first occurance fo e in the list L, assum that e is in L'''
    for i in range(len(L)):
        if L[i] == e:
            return i












