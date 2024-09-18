
def verif_carte(numero_carte):
    print("On est dans la fonction")
    print(numero_carte)
    # On transforme le numéro de la carte saisie en un tableau d'entiers
    tableau = [int(i) for i in str(numero_carte)]
    print("Contenu du tableau avant calculs : ", tableau)
    # On parcourt le tableau
    for i in range(0, 16, 2):
        tableau[i] *= 2
        if tableau[i] > 9:
           tableau[i] -= 9
    print("Contenu du tableau après calculs : ", tableau)

    # On calcule la somme des chiffres
    total = sum(tableau)
    print("Total :", total)

    # La carte est valide si la somme des chiffres est un multiple de 10
    return total % 10 == 0

# Algorithme principal
# carte_valide = verif_carte("valid_card_number = 4532015112830366")

carte_saisie = int(input("Saisir votre numéro de carte bancaire : "))
carte_valide = verif_carte(carte_saisie)
if carte_valide:
    print("La carte bancaire est valide.")
else:
    print("La carte bancaire n'est pas valide.")

