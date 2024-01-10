import os
import string


main.menu()

def list_of_files(directory, extension):
    speeches = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            speeches.append(filename)
    return speeches

def print_list(file_list):
    for file in file_list:
        print(file)

def extract_names(filename: str) -> str:
    # extract pres nom
    prefix = 'Nomination_'
    suffix = '.txt'
    start = filename.find(prefix) + len(prefix)
    end = filename.find(suffix)
    if start != -1 and end != -1:
        name = filename[start:end]
        # enlevez les nombres
        name = ''.join(char for char in name if not char.isdigit())
        return name.strip()  # enlevez les espaces

def nompresliste(folder: str) -> set:
    # list nom presidents
    all_names = set()
    for filename in os.listdir(folder):
        name = extract_names(filename)
        all_names.add(name)
    return all_names

# extraire nom presidents
directory = "./speeches"
nomunique = nompresliste(directory)
print("nom des president):", nomunique)


def lowercase():
    # convertion speeches en minuscule en fichier clean
    cleanversion = 'clean'

    if not os.path.exists(cleanversion):
        os.mkdir(cleanversion)

    for filename in os.listdir('speeches'):
        input_path = os.path.join('speeches', filename)
        output_path = os.path.join(cleanversion, filename)

        with open(input_path, 'r', encoding='utf-8') as file:
            data = file.read()

        with open(output_path, 'w', encoding='utf-8') as new:
            new.write(data.lower())

#appel de la commance
lowercase()
def prenomassocier(nom: str) -> str:
    # assoc nom prenom president
    prenompres = {
        "Sarkozy": "Nicolas",
        "Giscard_dEstaing": "Valéry",
        "Mitterrand": "François",
        "Hollande": "François",
        "Macron": "Emmanuel",
        "Chirac": "Jacques"
    }

    # boucle pour donner au pres un prenom
    if nom in prenompres:
        return prenompres[nom]


# liste nom pres
presidents = ['Sarkozy', 'Giscard_dEstaing', 'Mitterrand', 'Hollande', 'Macron', 'Chirac']
for president in presidents:
    prenom = prenomassocier(president)
    print(prenom)


def ponctuationc(input_path: str, output_path: str):
    # lire le fichier de base
    with open(input_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # enleve la ponctuation et les truc speciaux
    trans = str.maketrans("", "", string.punctuation)
    data_no_punctuation = data.translate(trans)

    #ecrire dans le clean
    with open(output_path, 'w', encoding='utf-8') as new:
        new.write(data_no_punctuation)

#utlisation fonction
if __name__ == "__main__":
    cleaned_directory = "clean"

    for filename in os.listdir(cleaned_directory):
        input_path = os.path.join(cleaned_directory, filename)
        output_path = os.path.join(cleaned_directory, filename)

        ponctuationc(input_path, output_path)



