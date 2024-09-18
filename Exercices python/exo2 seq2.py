print("algorithme  qui permet de saisir 10 entiers, et qui les range au fur et à mesure dans un tableau. ")
tableau=[]
for i in range (0,10,1):
    tableau.append(int(input("saisir entier:")))
    print(tableau[i])
print (tableau)