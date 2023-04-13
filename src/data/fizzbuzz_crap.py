for i in range(1, 101):
    th = bool(i % 3)
    fi = bool(i % 5)
    p = str(i) * (not (th or fi))
    p += 'Fizz' * (not th)
    p += 'Buzz' * (not fi)
    print(p)
    
