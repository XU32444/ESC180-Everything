def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(19))


# how an calls?
# at most 2^(n+1) 01

# at least 1 + 2 + 4 + ... + 2^(n/2) - 2^(n/2+1) - 1
# note: 2^(n/2) = sqrt(2)^n
# O(1.41^n)


# how many calls produced by fib(k)
# num of calls produced by fib(k-1) + num of calls produced by fib(k-2)+1

#nfibcalls(k) = nfibcalls(k-1) + nfibcalls(k-2) + 1
# so fibcalls(k) is approx. fib(k)

# can prove that fib(5) = round(phi^n/squrt(5)), phi = (1+squrt(5))/2 the goldne ratiophi = 1.61

























