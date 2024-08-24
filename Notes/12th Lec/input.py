

num = input("give me a number betweeen 1 and 10")

#print(num.isdigit())
#print("lassdasd".isdigit())

def get_num_1_10():
    num = input("give me a number betweeen 1 and 10")
    if num.isdigit():
        if int(num)>= 1 and int(num)<= 10:
            return int(num),True
    return num,False


num,input_correct = get_num_1_10()
while not input_correct:
    num,input_correct = get_num_1_10()
print(num)



input_correct = False
num = input("give me a number betweeen 1 and 10")
if num.isdigit():
    if int(num) >= 1 and int(num) <= 10:
        input_correct = True
while not input_correct:
    num = input("give me a number between 1 and 10")
    if num.isdigit():
        if int(num)>= 1 and int(num) <= 10:
            input_currect = True
print("The input was; ", num)