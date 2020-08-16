def es_primo(num):
    if int(num) <= 1:
        return False
    else:
        for x in range(2,num):
            if num % x == 0 and 1 != num:
                return False
        return True