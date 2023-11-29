import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extract_names(filename: str) -> str:
    # etraire nom des présidents des fichiers
    if 'speeches' in filename:
        f = filename.split('speeches/Nomination_')
    else:
        f = filename.split('Nomination_')
    if '1' in f[1]:
        a = f[1].split('1.txt')
        return str(a[0])
    elif '2' in f[1]:
        a = f[1].split('2.txt')
        return str(a[0])
    else:
        a = f[1].split('.txt')
        return str(a[0])


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
            new.write(data.lower())


