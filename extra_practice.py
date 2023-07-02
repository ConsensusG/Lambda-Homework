print((lambda poi: poi + 2)(890))


squeeky = lambda f, y: f*y
print(squeeky(3,4))


def stinko(man, y):
    print(man(y))

stinko(lambda man: man * 5, 20)


def stinky_lam(x,y):
    return lambda a, b: a + b + x + y

lambacious = stinky_lam(2,3)
print(lambacious(4,5))

lumpy_bump = lambda x: x + 30 if x < 10 else x + 1

print(lumpy_bump(7))
print(lumpy_bump(5))
print(lumpy_bump(20))
print(lumpy_bump(30))