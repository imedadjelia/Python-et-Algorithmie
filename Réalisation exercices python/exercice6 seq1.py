print("calcul du montant de la facture")
NPh= float(input("entrez le nombre de photocopie:"))
if NPh<=10:
     print (NPh*0.1)

elif 11<NPh<=20:
     print (NPh*0.08)
elif 21<NPh<=50:
     print (NPh*0.06)
elif    NPh>=51: 
     print (NPh*0.03)