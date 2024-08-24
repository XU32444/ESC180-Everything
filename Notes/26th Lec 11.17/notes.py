a = 10

for i in range(k1):
    for s in range(k2):
        a = a*20

# float operations : are constant
# int operations : not necessary

# how many iterations? k1 * k2
# runtime = O(k1*k2)

# Recipie for complexicity analysis
# 1. identify whta we are counting such as :
# iterations(assume every iteration takes the same time), operations,

# a particular operation, (e.g. comparisons, assuming tha thte number of comparsons is proportional to the run time)
# 2. write the formula for the thing you are counting
# 3. simplify and write big-oh notation

##
#linear search O(n)
#go through each element in a list
#biinary search Olog2(n)

# logest sequence consisting
# of "a" s ina string a s
# s = "abaaaaanax" -> 5
d = "aaaabbbabbsbabsdbasdbasda"
def longest(s):
    for length in range(len(s), 1, -1):
        if "a" * length in s:
            return length
        return 0
longest(d)
# not O(len(s)) O(n), n = len(s)
def num_as_in_s(s):
    counter = 0
    max_counter = 0
    s = s + "b"
    for letter in s:
        if letter == "a":
            connter = counter + 1
            # if counter == n:
            #     return True
        else:
            if counter > max_counter:
                max_counter = counter
                counter = 0
    return max_counter
    # finite-state machine
# worst case: O(len(s))
# best case = O(1)

def longest_seq(s):
    for length in range(len(s), -1, -1):
        if n_as_in_s(s, length): # c * len(s) operations
            return length
    return 0

# Total: ~c * len(s) ^ 2 operations
# O(n^2) for n = len(s)






































