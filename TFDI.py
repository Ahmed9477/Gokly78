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
exemple_texte = "messieurs les présidents mesdames messieurs en ce jour où je prends la responsabilité dassumer la plus haute charge de letat je me sens dépositaire dune espérance lélection présidentielle na pas vu la victoire dune france contre une autre dune idéologie contre une autre elle a vu la victoire dune france qui veut se donner les moyens dentrer forte et unie dans le troisième millénaire le 7 mai le peuple français a exprimé sa volonté de changement je suis décidé à placer le septennat qui commence sous le signe de la dignité de la simplicité de la fidélité aux valeurs essentielles de notre république je naurai dautre ambition que de rendre les français plus unis plus égaux et la france plus allante forte de son histoire comme de ses atouts je ferai tout pour quun etat impartial assumant pleinement ses missions de souveraineté et de solidarité soit pour les citoyens le garant de leurs droits et le protecteur de leurs libertés je ferai tout pour que notre démocratie soit affermie et mieux équilibrée par un juste partage des compétences entre lexécutif et le législatif ainsi que lavait voulu le général de gaulle fondateur de la vème république le président arbitrera fixera les grandes orientations assurera lunité de la nation préservera son indépendance le gouvernement conduira la politique de la nation le parlement fera la loi et contrôlera laction gouvernementale telles sont les voies à suivre je veillerai à ce quune justice indépendante soit dotée des moyens supplémentaires nécessaires à laccomplissement de sa tâche surtout jengagerai toutes mes forces pour restaurer la cohésion de la france et renouer le pacte républicain entre les français lemploi sera ma préoccupation de tous les instants la campagne qui sachève a permis à notre pays de se découvrir tel quil est avec ses cicatrices ses fractures ses inégalités ses exclus mais aussi avec son ardeur sa générosité son désir de rêver et de faire du rêve une réalité la france est un vieux pays mais aussi une nation jeune enthousiaste prête à libérer le meilleur dellemême pour peu quon lui montre lhorizon et non létroitesse de murs clos le président françois mitterrand a marqué de son empreinte les quatorze ans qui viennent de sécouler un nouveau septennat commence je voudrais quà lissue de mon mandat les français constatent que le changement espéré a été réalisé je voudrais que plus assurés de leur avenir personnel tous nos compatriotes se sentent partie prenante dun destin collectif je voudrais que ces années lourdes denjeux mais ouvertes à tous les possibles les voient devenir plus confiants plus solidaires plus patriotes et en même temps plus européens car la force intérieure est toujours la source dun élan vers lextérieur avec laide des hommes et des femmes de bonne volonté conformément à lesprit et à la lettre de nos institutions et aussi à lidée que je me fais de ma mission je serai auprès des français garant du bien public en charge des intérêts supérieurs de la france dans le monde et de luniversalité de son message vive la république vive la france"
with open("clean/Nomination_Chirac1.txt", 'r', encoding='utf-8') as fichier:
    texte= fichier.read()


resultat_tf = tf(texte)



print("TF:", resultat_tf)


# Calcul du TF pour une liste de noms de fichiers
def calculer_tf(file_names):
    matrice = []
    repertoire_courant = os.getcwd()
    for nom_fichier in file_names:
        chemin_fichier = os.path.join('clean', nom_fichier)

        with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
            texte = fichier.read()
            freq_mot = tf(texte)
        matrice.append(freq_mot)
    return matrice


# Exemple d'utilisation de la fonction calculer_tf
exemple_file_names = ["Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt", "Nomination_Macron.txt", "Nomination_Mitterrand1.txt", "Nomination_Mitterrand2.txt", "Nomination_Sarkozy.txt"]
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
