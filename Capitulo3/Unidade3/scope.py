x = 10
y = 11 # corresponde a G
def foo():
    x = 20 # função foo corresponde a L
    print(x, y)
def bar():
    a = 30 #A função bar corresponde a E
    print(a, x, y) # cada variável corresponde a L, E e G
x = 40
foo()
bar()