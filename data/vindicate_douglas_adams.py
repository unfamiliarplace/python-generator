def any_base_to_int(n: str, base: int) -> int:
    result = 0
    mult = 1

    for i in range(len(n)):
        digit = int(n[-(i + 1)])
        result += digit * mult
        mult *= base

    return result

def vindicate_douglas_adams():
    assert 6 * 9 == any_base_to_int('42', 13)
