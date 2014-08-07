def f(x, square):
    return x**2.0 - square

def f_prime(x): return 2.0*x

def find_root(square, guess):
    imaginary = False
    if square < 0.0:
        imaginary = True
        square *= (-1)
    x = abs(float(guess))
    if x == 0.0: x+=1
    x0 = float
    while x0 != x:
        x0 = x
        x = x - f(x, square)/f_prime(x)
    return str(x) + ' i'*imaginary
