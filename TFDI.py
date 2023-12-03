import os
import math

# Calcul du TF pour une chaîne de caractères
def tf(texte):
    mots = texte.split()
    freq_mot = {}
    for mot in mots:
        if mot in freq_mot:
            freq_mot[mot] += 1
        else:
            freq_mot[mot] = 1
    return freq_mot

# Exemple d'utilisation de la fonction TF
exemple_texte = "Ceci est un exemple de texte pour le calcul du TF."
resultat_tf = tf(exemple_texte)
print("TF:", resultat_tf)

# Calcul du TF pour une liste de noms de fichiers
def calculer_tf(file_names):
    matrice = []
    repertoire_courant = os.getcwd()
    for nom_fichier in file_names:
        chemin_fichier = os.path.join('cleaned_lower_case_no_punctuation', nom_fichier)
        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            texte = fichier.read()
            freq_mot = tf(texte)
        matrice.append(freq_mot)
    return matrice

# Exemple d'utilisation de la fonction calculer_tf
exemple_file_names = ["fichier1.txt", "fichier2.txt"]
resultat_calculer_tf = calculer_tf(exemple_file_names)
print("Matrice TF:", resultat_calculer_tf)

# Calcul de l'IDF pour une matrice TF
def calculer_idf(matrice):
    compteur_idf = {}
    idf = {}
    for i in range(len(matrice)):
        for cle in matrice[i]:
            if cle in compteur_idf:
                compteur_idf[cle] += 1
            else:
                compteur_idf[cle] = 1
    for cle in compteur_idf:
        idf[cle] = math.log10((len(matrice) / compteur_idf[cle]))
    return idf

# Exemple d'utilisation de la fonction calculer_idf
resultat_idf = calculer_idf(resultat_calculer_tf)
print("IDF:", resultat_idf)

# Calcul du TF-IDF pour une liste de noms de fichiers
def calculer_tf_idf(tf, idf, file_names):
    file_names = ["'"] + file_names
    tf_idf = []
    tf_idf.append(file_names)
    for cle1 in idf:
        lst = [cle1]
        for ligne in tf:
            if cle1 not in ligne:
                lst.append(0.0)
            else:
                lst.append(ligne[cle1] * idf[cle1])
        tf_idf.append(lst)
    return tf_idf

# Exemple d'utilisation de la fonction calculer_tf_idf
resultat_tf_idf = calculer_tf_idf(resultat_calculer_tf, resultat_idf, exemple_file_names)
print("Matrice TF-IDF:", resultat_tf_idf)
