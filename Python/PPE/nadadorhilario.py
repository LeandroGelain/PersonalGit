i = int(input("Idade: "))

if i >= 5 and i <= 7:
    print('Infantil A')

elif i >= 8 and i <= 11:
    print('Infantil B')

elif i >= 12 and i <= 13:
    print('Juvenil A')

elif i >= 14 and i <= 17:
    print('Juvenil B')

elif i > 18 and i < 60: 
    print('Adulto')

elif i < 5:
    print('Bebe chorão, sai daqui!')

else:
    print('Ta fazendo hora extra na terra em...')