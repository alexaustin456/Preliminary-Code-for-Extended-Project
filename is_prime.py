def is_prime():
    a = 2
    num = int(input("Number:"))
    while num > a:
        if num % a == 0 & a != num:
            return False
        a += 1
    else:
        return True

is_prime()
