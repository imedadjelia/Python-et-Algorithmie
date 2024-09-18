print("prix après augmentation")
PU= float(input("le prix unitaire est de:"))
if PU<20:
 PA= float((PU*10)/100)
 print ("le prix après augmentation est de:",PU+PA)

elif 20<=PU<50:
 PA= float((PU*7.5)/100)
 print ("le prix après augmentation est de:",PU+PA)

elif 50<=PU<100:
 PA= float((PU*5)/100)
 print ("le prix après augmentation est de:",PU+PA)

else :
 PA= float((PU*2.5)/100)
 print ("le prix après augmentation est de:",PU+PA)
