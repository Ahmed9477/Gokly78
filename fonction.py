import os

def extract_names(filename: str) -> str:
    # Extraire le nom des présidents des fichiers
    if 'speeches' in filename:
        f = filename.split('speeches/Nomination_')
    else:
        f = filename.split('Nomination_')

    # Identifier le numéro dans le nom du fichier
    if '1' in f[1]:
        a = f[1].split('1.txt')
    elif '2' in f[1]:
        a = f[1].split('2.txt')
    else:
        a = f[1].split('.txt')

    return str(a[0])

def clean_filename(filename: str) -> str:
    # Supprimer les caractères indésirables du nom du fichier
    cleaned_name = filename.replace('1', '').replace('2', '').replace('.txt', '').replace('_', ' ')
    return cleaned_name

# Liste des noms de fichiers
noms_fichiers = ['Nomination_Chirac1.txt', 'Nomination_Chirac2.txt', 'Nomination_Mitterrand2.txt', 'Nomination_Sarkozy.txt', 'Nomination_Mitterrand1.txt', 'Nomination_Hollande.txt', 'Nomination_Macron.txt', 'Nomination_Giscard dEstaing.txt']

# Utiliser la fonction extract_names pour extraire les noms
extracted_names = [extract_names(nom) for nom in noms_fichiers]

# Utiliser la fonction clean_filename pour nettoyer les noms extraits
cleaned_names = [clean_filename(name) for name in extracted_names]

# Utiliser un ensemble pour obtenir les prénoms uniques
Poureviterdoublage = set(cleaned_names)






def list_names(folder: str) -> list:
    # lister le nom des président en liste
    L = []
    A = os.listdir(folder)
    for k in range(len(A)):
        if extract_names(A[k]) not in L:
            L.append(extract_names(A[k]))
    return L


def lowercase():  # convertie en minuscule
    # version modif des docs
    try:
        os.mkdir('modif')
    except FileExistsError:
        pass
    A = os.listdir('speeches')
    # copier coller dans un autre fichier en majuscule
    for i in range(len(A)):
        with open(f'speeches/{A[i]}', 'r+', encoding='utf-8') as file:
            data = file.read()
            new = open(f'modif/{A[i]}', 'w+', encoding='utf-8')


