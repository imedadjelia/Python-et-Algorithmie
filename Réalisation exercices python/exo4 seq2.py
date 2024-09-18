print("Algorithme inverseur des valeurs contenues dans un tableaude 10 entiers")
tableau=[5,9,3,8,14,22,87,96,14,10]
for i in range (0,5,1):
    v=tableau[i]
    tableau[i]=tableau[9-i]
    tableau[9-i]=v
print(tableau)



