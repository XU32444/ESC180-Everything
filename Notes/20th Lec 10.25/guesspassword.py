
def guess_password(password):
    return password == "g5a!"

#ASCII (aski)
# a way of numbering characters useing nubers 0..127
#look up the ASCII character i using chr[i]
for i in range(128):
    print(chr[i])

alphabet = ""
for i in range(128):
    alphabet = alphabet + chr[i]

for c1 in alphabet:
    for c2 in alphabet:
        for c3 in alphabet:
            for c4 in alphabet:
                print(f"Trying {c1 + c2 + c3 + c4}")
                if guess_password(c1+c2+c3+c4):
                    print("Guessed it!")
                    input("Enter anything to continur")


L = [5, 6, 7]
for i in range(len(L)):
    print(L[i])
for e in L:
    print(e)

alphabet = ""
for i in range(128):
    alphabet = alphabet + char(i)

for c1 in alphabet:
    for c2 in alphabet:
        for c3 in alphabet:



def make_nested_loop(n):
    res = "def guess_passwords(alphabet):\n"
    for i in range(1, n+1):
        res = res + f"{4*i*''}for c{i} in alphabet:\n"

    res = res + (n+1) * '' * 4 + "print("
    for i in range(1, n+1):
        res += f"c{i} + "
    res += "+ '' )"
    return res

code = make_nested_loop(10)
print(code)






