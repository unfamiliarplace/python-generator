def off_square(lower: int, distance: int) -> int:
    upper = lower + distance
    mean = lower + (distance / 2)
    return mean**2 - (lower * upper)

def test(upper: int) -> None:
    for n in range(1, upper + 1):
        for distance in range(0, 9):
            off = off_square(n, distance)
            if off != (distance / 2)**2:
                print(f'{n} * {n+(distance * 2)} is {off} less than {n+distance}^2')

test(1000)

# 16 x 16 = 0 less than 16 x 16
# 15 x 17 = 1 less than 16 x 16
# 14 x 18 = 4 less than 16 x 16
# 13 x 19 = 9 less than 16 x 16

# Moreover, even with non-integer means
# 15 x 16 = 0.25 less than 15.5 x 15.5
# 15 x 18 = 2.25 less than 16.5 x 16.5

# Square the distance from the middle #

# For any two numbers a and b, let c be their average.
# The product of any two numbers is
# equal to the square of their mean minus the square of half their range.
