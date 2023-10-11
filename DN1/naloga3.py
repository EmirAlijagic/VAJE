'''
Uporabnika vprašajte za 3 celoštevilske vrednosti in jih izpišite s pomočjo print() in type(). 
V eni vrstici preverite, ali je druga vrednost enaka prvi, in ali je tretja vrednost manjša ali enaka prvi.
'''
x, y, z = input("Vnesi 3 cela števila: ").split()
print("x: ", x, type(x))
print("y: ", y, type(y))
print("z: ", z, type(z))

if(x==y and z<=x):
    print("Prva vrednost je enaka drugi. In tretja vrednost je manjša ali enaka prvi.")