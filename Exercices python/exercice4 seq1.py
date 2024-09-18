print("application de remise sur produit")
qte= float(input("saisir la qte:"))
print(qte)
PUHT=float(input("saisir le PUHT:"))
THT= qte*PUHT
print("le THT est de:", THT)
if THT<200:
    print ("prix THT avec remise est de:",THT*(1-2.5/100))
elif 200<=THT<400: 
    print ("prix THT avec remise est de:",THT*(1-5/100))
elif 400<=THT<700: 
    print ("prix THTavec remise est de:",THT*(7.5-5/100))
elif 700<=THT: 
    print ("prix THT avec remise est de:",THT*(1-10/100))






