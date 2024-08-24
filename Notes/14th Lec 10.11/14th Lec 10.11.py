# import my_random
#
# if __name__=='__main__':
#     my_random.seed(5)
#     print(random.random())
def username_matches_password(username,password,usernames,passwords):
    if username not in usernames:
        return False
    actual_password =  passwords[usernames.index(username)]
    return password == actual_password

def login(username,password):
    global locked_out
    global login_attempts
    if username_matches_password(username,password,usernames,passwords) and not login_attempts[username.index(username)] >= 3:
        return True
    else:
        if username in usernames:
            login_attempts[usernames.index(username)] += 1
        #     return False
        # else:
        #     return False
        return False

def add_user(username,password):
    usernames.append(username)
    passwords.append(password)







usernames = ["Cluett","Stangeby","Guerzhoy"]
passwords = ["matrix","rigorous","asd"]
login_attempts = [0, 0, 0]

if __name__ == '__main__':
    print(login("Cluett","vector"))
    print(login("Cluettt","vector"))
    print(login("Cluettt","vector"))
    print(login("Cluettt","matrix"))
    print(login("Stangeby","rigorous"))