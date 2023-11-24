with open("fichierTest.txt", "r") as f :
    contenu = f.readlines()
for ligne in contenu:
    print(ligne)