print("Hello world")
"""
x = range(-5, 10, 1)
print(type(x))
print(list(x))
for number in range(1,20,2):
    print(number)


kvadrat = lambda x: x**2
"""
# TRIKOTNIK


def trikotnik(s):
    i = 1
    print(" " *(s-i),"*" *i," " *(s-i))
    i = 0
    for x in range(s):
        i = i + 1
        
        print(" " *(s-i),"*" *i*2," " *(s-i))

trikotnik(6)