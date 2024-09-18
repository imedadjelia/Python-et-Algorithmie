# Factorielle simple
def factorielle(v): 
    if v < 0: 
        print("La factorielle d'un nombre négatif n'existe pas")
    elif v == 0: 
        return 1
    else: 
        f = 1
        while(v > 1): 
            f *= v 
            v -= 1
        return f

# Algorithme principal
v = int(input("Saisir un entier : "))
print("La factorielle de",v,"est", factorielle(v))



################################################


# Factorielle récursive
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)

# Algorithme principal
v = int(input("Saisir un entier : "))
print("La factorielle de",v,"est", factorielle(v)) 


###############"########################"""

# Fibonacci récursive
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return fibonacci(n - 2) + fibonacci(n - 1)

# Algorithme principal
nb = int(input("Saisir le nombre d'entiers à afficher : "))
print("Les", nb, "premiers entiers de la suite de Fibonacci sont :")
for i in range(nb):
    print(fibonacci(i), end = " ")

