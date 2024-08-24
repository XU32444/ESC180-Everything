# Strings

"abc"

"abc" + "def"

s = "abc"
s.find("b")

for letter in s:
    print(letter)

s[1] # b
s = "123"
s.isdigit()

s = "engsci"
s.capitalize()# by itself, probably wrong cuz it wont change s, and doesnt store the result of s.capitalize() anywhere

s = s.capitalize()#makes sennse
s_capitalized = s.capitalize()#makes sense
#cannot do s[0] = "E"

address_num = 40
street = "St. George St"
str(address_num) + " " + street

# f-strings (f for format)
f"{address_num}{street}"


