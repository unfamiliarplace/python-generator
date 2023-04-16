def m_to_d_1(m: int) -> int:
    """Hardcoding each relation"""

    if m == 1:
        return 31
    elif m == 2:
        return 28
    elif m == 3:
        return 31
    elif m == 4:
        return 30
    elif m == 5:
        return 31
    elif m == 6:
        return 30
    elif m == 7:
        return 31
    elif m == 8:
        return 31
    elif m == 9:
        return 30
    elif m == 10:
        return 31
    elif m == 11:
        return 30
    elif m == 12:
        return 31


def m_to_d_2(m: int) -> int:
    """Hardcoding each relation, but code golfed"""
    
    return int('312831303130313130313031'[(m - 1) * 2:][:2])

def m_to_d_3(m: int) -> int:
    """First attempt to find a pattern"""
    
    if m == 2:
        return 28
    elif m < 8:
        return 30 + m % 2
    else:
        return 31 - m % 2

def m_to_d_4(m: int) -> int:
    """Same as 3 but as an expression instead of with control keywords"""

    return 28 + (2 * (m != 2)) + ((m < 8 and m % 2) or (m > 7 and not (m % 2)))



months = list(range(1, 13))
check = [m_to_d_1(m) for m in months]
test = [m_to_d_4(m) for m in months]
print(check == test)
