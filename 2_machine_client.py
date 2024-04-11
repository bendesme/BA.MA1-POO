import json

# Fonction principale pour poser la question et gérer les réponses
def interaction_première():
    print("\nQuel livre recherchez-vous ?")
    rechercher_livre()

#RECHERCHER UN LIVRE
def rechercher_livre():
    print("\nRecherche de livre :")

    # Charger le contenu du fichier JSON dans une structure de données Python
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Demander à l'utilisateur les critères de recherche
    critere_recherche = input("Entrez le titre, l'auteur, l'ISBN ou l'éditeur du livre que vous recherchez : ").strip().lower()

    # Créer une liste pour stocker les résultats de la recherche
    resultats = []

    # Parcourir chaque livre dans la base de données pour vérifier les critères de recherche
    for livre in data:
        if critere_recherche in livre['Titre'].lower() \
            or critere_recherche in livre['Auteur'].lower() \
            or critere_recherche in livre['ISBN'].lower() \
            or critere_recherche in livre['éditeur'].lower():
            resultats.append(livre)

    # Afficher les résultats de la recherche
    if resultats:
        print("\n Résultats de la recherche :")
        for livre in resultats:
            print(f"\nTitre: {livre['Titre']}")
            print(f"Auteur: {livre['Auteur']}")
            print(f"ISBN: {livre['ISBN']}")
            print(f"Quantité: {livre['quantité']}")
            print(f"Éditeur: {livre['éditeur']}")
            print(f"Prix: {livre['prix']}€\n")
    else:
        print("\nAucun livre trouvé correspondant à votre recherche.\n")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            interaction_première()
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")

# Appel de la fonction principale pour démarrer l'interaction avec le client
if __name__ == "__main__":
    print("\nBienvenu.e !")
    interaction_première()