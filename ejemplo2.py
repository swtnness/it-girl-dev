def generador():
    n = 1
    yield n   
    n+= 1
    yield n   
    n+= 1
    yield n
    
g = generador()
print(next(g))
print(next(g))
print(next(g))