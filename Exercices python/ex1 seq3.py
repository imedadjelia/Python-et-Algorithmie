print("Calculette")

# Contrôle de la première variable
while True:
    try:
        v = input("Veuillez saisir un nombre : ")
        resultat = float(v)
        break
    except ValueError:
        print("Saisie incorrecte")
# Fin du contrôle de la première variable 

# Boucle "infinie" dont on sort par la saisie du mot "stop"
while True:
    op = str(input("Saisir une opération + - * / ou 'stop' pour arrêter : "))

# Contrôle de la saisie de l'opération ou du mot stop    
    while op != '+' and op != '-' and op != '*' and op != '/' and op != 'stop':
        print("Saisie incorrecte")
        op = str(input("Saisir une opération + - * / ou stop pour arrêter : "))
# Fin du contrôle de la saisie de l'opération ou du mot stop  
      
    if op == 'stop':
        break   # Sortie de la boucle grâce au mot "stop", on sort du programme
    else:
        # Contrôle de la seconde variable
        while True:
            try:
                v = input("Veuillez saisir un nombre : ")
                n = float(v)
                break
            except ValueError:
                print("Saisie incorrecte")
        # Fin du contrôle de la seconde variable
        if op == '/':
            if n == 0:
                print("Division par 0 impossible")
                # Contrôle de la division par zéro
                while True:
                    try:
                        v = input("Veuillez saisir un nombre différent de 0 : ")
                        n = float(v)
                        if n != 0:
                            break
                    except ValueError:
                        print("Saisie incorrecte")
                # Fin du contrôle de la division par zéro
            resultat = resultat / n
        elif op == '+':
            resultat = resultat + n
        elif op == '-':
            resultat = resultat - n
        else:
            resultat = resultat * n
        print("Le résultat est :", resultat)