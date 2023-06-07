import random

uzvaras_spel = 0
uzvaras_dators = 0
vards = input('Ievadiet savu vārdu: ')
def speles_beigas():
    print(' ______                                             __')
    print('  / ____/___ _____ ___  ___     ____ _   _____  _____/ /')
    print(' / / __/ __ `/ __ `__ \/ _ \   / __ \ | / / _ \/ ___/ /')
    print('/ /_/ / /_/ / / / / / /  __/  / /_/ / |/ /  __/ /  /_/ ')
    print('\____/\__,_/_/ /_/ /_/\___/   \____/|___/\___/_/  (_)  ')

while True:
    speletajs = input('Ievadiet savu darbību (akmens, šķēres, papīrītis). Ja gribat pārtraukt spēli, ievadiet "beigas". ')
    darbibas = ['akmens', 'šķēres', 'papīrītis']
    dators = random.choice(darbibas)
    
    if speletajs == 'beigas':
        speles_beigas()
        print(f'{vards}: {uzvaras_spel}')
        print(f'Dators: {uzvaras_dators}')
        break
    
    print(f'\n{vards}, jūsu izvēle ir {speletajs}, datora izvēle ir {dators}.\n')

    if speletajs == dators:
        print(f'Abu spēlētāju izvēle ir {speletajs}. Uzvarētāja nav.')
    elif speletajs == 'akmens':
        if dators == 'šķēres':
            print('Akmens sagrauj šķēres! Jūs uzvarat!')
            uzvaras_spel += 1
        else:
            print('Papīrs pārklāj akmeni! Jūs zaudējat.')
            uzvaras_dators += 1
    elif speletajs == 'papīrītis':
        if dators == 'akmens':
            print('Papīrs pārklāj akmeni! Jūs uzvarat!')
            uzvaras_spel += 1
        else:
            print('Šķēres griež papīru! Jūs zaudējat.')
            uzvaras_dators += 1
    elif speletajs == 'šķēres':
        if dators == 'papīrītis':
            print('Šķēres griež papīru! Jūs uzvarat!')
            uzvaras_spel += 1
        else:
            print('Akmens sagrauj šķēres! Jūs zaudējat.')
            uzvaras_dators += 1
    else:
        print('Tādas darbības nav! Jūs zaudējat.')
