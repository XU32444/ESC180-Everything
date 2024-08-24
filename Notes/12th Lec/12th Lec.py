import mymath
import sys
print("hi you are inporting" + __name__)

print(__name__)

#if __name__=="__main__":
#    print(mymath.square(6))
#    print(mymath.square(88))



if __name__=="__main__":
    if mymath.square(4) != 25:
        print("ERROR")
        sys.exit(1)



#naming varaiables:
#officially: anthign that starts a letter and contains letters, digits, and underscores
#            is a legal identifie(name of varibale, function, etc.)

#number of cups of cofffee
N = 12
print(N)



