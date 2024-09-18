def decalage_message(message, decalage, sens):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_modifie = ''
    
   
    if sens == 'inverse':
        alphabet = alphabet[::-1]
    
    for lettre in message:
        if lettre in alphabet:
            
            curseur = alphabet.index(lettre)
            curseur_dec = (curseur + decalage) % 26
            lettre_dec = alphabet[curseur_dec]
            
        
            message_modifie += lettre_dec
    
    return message_modifie


message = input("Veuillez saisir le message à décaler : ")
decalage = int(input("Veuillez saisir le décalage souhaité (nombre de caractères) : "))
sens = input("Veuillez saisir le sens du décalage (ordre ou inverse) : ") 
message_decale = decalage_message(message, decalage, sens)
print("Message après décalage :", message_decale)





