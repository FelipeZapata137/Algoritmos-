def poker(cartas):
    numeros = [carta[0] for carta in cartas]
    
    for numero in numeros:
        if numeros.count(numero) == 4:
            return True
    
    return False

mano = [(5, 'corazones'), (5, 'tréboles'), (5, 'picas'), (5, 'diamantes'), (10, 'corazones')]
print("¿Es póker?", poker(mano))

mano2 = [(2, 'corazones'), (3, 'tréboles'), (4, 'picas'), (5, 'diamantes'), (6, 'corazones')]
print("¿Es póker?", poker(mano2))