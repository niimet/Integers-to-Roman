# Integers-to-Roman

def crypt(data,k):
    if k == 0:
        return 1

    s = len(data) - k

    if data[s] == 0:
        return 0
    
    result = crypt(data, k - 1 )
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += crypt(data, k - 2 )
    
    return result

def roman(n):
    n = str(n)
    if len(n) == 1:
        return n
    st = f"{n[0]}"
    for digit in range(len(n)-1):
        st += "0"
    
    st += " "+roman(n[1:])
    
    
    return st

def helper(rum):
    rum = rum.split(" ")

    lens = [len(r) for r in rum]
    a = ""
    for r in rum:
        a += nums(r)
    
    return a

def nums(length):
    numitself = length
    length = len(length)
    
    if numitself[0] == "0":
        return ""
    
    if length == 1:
        bir = "I"
        bes = "V"
        on = "X"
    elif length == 2:
        bir = "X"
        bes = "L"
        on = "C"
    elif length == 3:
        bir = "C"
        bes = "D"
        on = "M"
    elif length == 4:
        bir = "M"
        bes = "D"
        on = "M"
    
    str_ = ""
    if int(numitself[0]) >= 1 and int(numitself[0]) <= 3:
        for roma in range(int(numitself[0])) :
            str_ += f"{bir}"

    elif int(numitself[0]) == 4:
        str_ += f"{bir}{bes}"

    elif int(numitself[0]) >= 5 and int(numitself[0]) <= 8:
        str_ = f"{bes}"

        for roma in range(5,int(numitself[0])):
            str_ += f"{bir}"

    elif int(numitself[0]) == 9:
        str_ += f"{bir}{on}" 
    elif int(numitself[0]) == 10:
        str_ += f"{on}"

    return str_
