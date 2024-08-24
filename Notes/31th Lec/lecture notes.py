
def fact_itr(n):
    res = 1
    for i in range(1,n+1):
        res = res * i
    return res

def fact_iter(n):
    res = 1
    i = 1
    while i < n:
        res = res * i
        i = i + 1
    return res


def fact_iter_rec(n,i,res):
    if not i <= n:
        return res
    else:
        return fact_iter_rec(n,i+1,res * i)


def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)



##


def is_win21(n):
    '''return true if getting to n means you wil win at race to 21 win perfect play'''
    if n >= 21:
        return True
    return not is_win(n+1) and not is_win(n+2)

print(is_win21(16))

def is_win_general(n, target, moves):
    if n > target:
        return False
    if n == target:
        return True
    for move in moves:
        if is_win_general(n+move,target,moves):
            return False
        return True

def is_win_state21(state):
    return state + move




def is_win_very_general(state,is_win_state,make_move):
    cur_win__state = is_win_state






























































