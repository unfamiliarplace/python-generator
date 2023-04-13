print(" ")
print("Guess the number. You may only enter numerals.")
print("...It is winnable. >:)")
print(" ")

a = 0

while a == 0:
    x = float(input("How many? "))
    if x > 17.5 and x != 71:
        print("Not enough.")
        print(" ")
    elif x < 17.5:
        print("Too many.")
        print(" ")
    else:
        print("Yeah!")
        print("A chocolate bar is totally coming your way.")
        print("Any time now.")
        a = 1
        
input()