import math
x = 0.7
e = 0.01
s = 0
n = 1
term = math.sin(x**n)
while abs(term) >= e:
    if n % 2 == 1:
        s += term
    else:  
        s -= term
    n += 1
    term = math.sin(x**n)
print(s)
