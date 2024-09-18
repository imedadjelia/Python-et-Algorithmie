def decalage_message(message, decalage, sens):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    message_modifie = ''
    
   
    if sens == 'inverse':
        alphabet = alphabet[::-1]
    
    for lettre in message:
        if lettre.lower() in alphabet:
            is_upper = lettre.isupper()
            curseur = alphabet.index(lettre.lower())
            curseur_dec = (curseur + decalage) % 26
            lettre_dec = alphabet[curseur_dec]
            if is_upper:
                lettre_dec = lettre_dec.upper()
            message_modifie += lettre_dec
        else:
            message_modifie += lettre 
    
    return message_modifie


message = input("Veuillez saisir le message à décaler : ")
decalage = int(input("Veuillez saisir le décalage souhaité (nombre de caractères) : "))
sens = input("Veuillez saisir le sens du décalage (ordre ou inverse) : ").lower()


if sens not in ['ordre', 'inverse']:
    print("Le sens du décalage n'est pas valide. Veuillez saisir 'ordre' ou 'inverse'.")
else:
    
    message_decale = decalage_message(message, decalage, sens)
    print("Message après décalage :", message_decale)
