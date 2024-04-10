import json

# Fonction principale pour poser la question et gérer les réponses
def interaction_première():
    print("1. Rechercher un livre")
    print("2. Encaisser un livre")
    print("3. Ajouter un livre au stock")
    print("4. Modifier un livre du stock")
    print("5. Supprimer un livre du stock")
    print("6. Quitter le menu\n")
    choix = input("Choisissez une option : 1, 2, 3, 4, 5 ou 6 : ")

    if choix == '1':
        rechercher_livre()
    elif choix == '2':
        encaisser_livre()
    elif choix == '3':
        ajouter_livre()
    elif choix == '4':
        modifier_livre()
    elif choix == '5':
        supprimer_livre()
    elif choix == '6':
        print("\nVous avez quitté le menu.\n")
    else:
        print("Option invalide. Veuillez choisir une option valide : 1, 2, 3, 4, 5 ou 6 : ")
        interaction_première()

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
            rechercher_livre()
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")

#ENCAISSER UN LIVRE
# Fonction pour rechercher un livre par titre
def rechercher_livre_par_titre(titre_recherche):
    with open('data.json', 'r') as f:
        data = json.load(f)

    for livre in data:
        if titre_recherche.lower() in livre['Titre'].lower():
            return livre, data

    return None, None

# Fonction pour encaisser un livre
def encaisser_livre():
    print("\nEncaissement d'un livre :")
    titre = input("Entrez le titre du livre à encaisser : ")

    livre, data = rechercher_livre_par_titre(titre)

    if livre and data:
        print("\n\nEst-ce bien ce livre que vous voulez encaisser ?")
        print(f"\nTitre: {livre['Titre']}")
        print(f"Auteur: {livre['Auteur']}")
        print(f"ISBN: {livre['ISBN']}")
        print(f"Quantité: {livre['quantité']}")
        print(f"Éditeur: {livre['éditeur']}")
        print(f"Prix: {livre['prix']}€\n")
        print("1. Oui")
        print("2. Non")
        print("3. Quitter le menu")
        
        choix = input("Choisissez une option : 1, 2 ou 3 : ")
        if choix == '1':
            if livre['quantité'] > 0:
                    livre['quantité'] -= 1
                    print(f"\nUn exemplaire de '{livre['Titre']}' a été encaissé. Nouvelle quantité : {livre['quantité']}")
                    print(f"\nprix à payer pour ce livre : '{livre['prix']}€")
                    if livre['quantité'] == 0:
                         print("\nAttention : Ce livre est maintenant Sold Out.\n")
                    # mettre à jour le fichier Json
                    with open('data.json', 'w') as f:
                        json.dump(data, f, indent=4)
            else:
                print("\nDésolé, ce livre est déjà Sold Out.\n")
        elif choix == '2':
            encaisser_livre()
        elif choix == '3':
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide. Veuillez recommencer.\n")
            encaisser_livre()
    else:
        print(f"Le livre avec le titre '{titre}' n'a pas été trouvé dans la base de données.")

#AJOUTER UN LIVRE
def ajouter_livre():
    print("Ajout d'un nouveau livre :")
    titre = input("Titre du livre : ")
    auteur = input("Auteur du livre : ")
    isbn = input("ISBN du livre : ")
    quantite = int(input("Quantité disponible : "))
    editeur = input("Éditeur du livre : ")
    prix = float(input("Prix du livre : "))

    nouveau_livre = {
        "ID": len(data) + 1,  # Générer un nouvel ID en fonction de la longueur actuelle de la liste
        "Titre": titre,
        "Auteur": auteur,
        "ISBN": isbn,
        "quantité": quantite,
        "éditeur": editeur,
        "prix": prix
    }

    # Charger le contenu du fichier JSON existant
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Ajouter le nouveau livre à la liste existante
    data.append(nouveau_livre)

    # Écrire les données mises à jour dans le fichier JSON
    with open('data.json', 'w') as f:
        json.dump(data, f)

    print("Livre ajouté avec succès !")

#MODIFIER UN LIVRE
def modifier_livre():
    print("Liste des titres des livres :")

    # Charger le contenu du fichier JSON dans une structure de données Python
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Afficher la liste des titres des livres
    for livre in data:
        print(f"ID: {livre['ID']}, Titre: {livre['Titre']}")

    # Demander à l'utilisateur de choisir l'ID du livre à modifier
    id_livre = input("Entrez l'ID du livre à modifier : ")

    # Rechercher le livre par ID
    livre_a_modifier = None
    for livre in data:
        if str(livre['ID']) == id_livre:
            livre_a_modifier = livre
            break

    # Si le livre est trouvé, permettre à l'utilisateur de modifier ses informations
    if livre_a_modifier:
        print(f"Livre trouvé : {livre_a_modifier['Titre']}")
        nouveau_titre = input("Entrez le nouveau titre (laissez vide pour ne pas modifier) : ").strip()
        nouveau_auteur = input("Entrez le nouvel auteur (laissez vide pour ne pas modifier) : ").strip()
        nouveau_ISBN = input("Entrez le nouvel ISBN (laissez vide pour ne pas modifier) : ").strip()
        nouvelle_quantite = input("Entrez la nouvelle quantité (laissez vide pour ne pas modifier) : ").strip()
        nouveau_editeur = input("Entrez le nouvel éditeur (laissez vide pour ne pas modifier) : ").strip()
        nouveau_prix = input("Entrez le nouveau prix (laissez vide pour ne pas modifier) : ").strip()

        # Mettre à jour les informations du livre si l'utilisateur a fourni de nouvelles valeurs
        if nouveau_titre:
            livre_a_modifier['Titre'] = nouveau_titre
        if nouveau_auteur:
            livre_a_modifier['Auteur'] = nouveau_auteur
        if nouveau_ISBN:
            livre_a_modifier['ISBN'] = nouveau_ISBN
        if nouvelle_quantite:
            livre_a_modifier['quantité'] = int(nouvelle_quantite)
        if nouveau_editeur:
            livre_a_modifier['éditeur'] = nouveau_editeur
        if nouveau_prix:
            livre_a_modifier['prix'] = float(nouveau_prix)

        # Enregistrer les modifications dans le fichier JSON
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Livre modifié avec succès.")
    else:
        print(f"Aucun livre trouvé avec l'ID '{id_livre}'.")

#SUPPRIMER UN LIVRE
def supprimer_livre():
    print("Liste des titres des livres :")

    # Charger le contenu du fichier JSON dans une structure de données Python
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Afficher la liste des titres des livres
    for livre in data:
        print(f"ID: {livre['ID']}, Titre: {livre['Titre']}")

    # Demander à l'utilisateur de choisir l'ID du livre à supprimer
    id_livre = input("Entrez l'ID du livre à supprimer : ")

    # Rechercher le livre par ID
    livre_a_supprimer = None
    for livre in data:
        if str(livre['ID']) == id_livre:
            livre_a_supprimer = livre
            break

    # Si le livre est trouvé, demander confirmation à l'utilisateur avant de le supprimer
    if livre_a_supprimer:
        print(f"Livre trouvé : {livre_a_supprimer['Titre']}")
        confirmation = input("Voulez-vous vraiment supprimer ce livre ? (o/n) : ").strip().lower()

        if confirmation == 'o' or confirmation == 'oui':
            # Supprimer le livre de la liste
            data.remove(livre_a_supprimer)

            # Enregistrer les modifications dans le fichier JSON
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Livre supprimé avec succès.")
        else:
            print("Suppression annulée.")
    else:
        print(f"Aucun livre trouvé avec l'ID '{id_livre}'.")

# Appel de la fonction principale pour démarrer l'interaction avec le client
if __name__ == "__main__":
    interaction_première()