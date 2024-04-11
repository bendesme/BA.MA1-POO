import requests
import json

# Définition de la classe parent "Livre"
class Livre:
    def __init__(self, titre, auteur, isbn, quantite, editeur, prix):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.quantite = quantite
        self.editeur = editeur
        self.prix = prix

    def __str__(self):
        return f"{self.titre} par {self.auteur}"

# Définition de la classe enfant "Manga" qui hérite de la classe "Livre"
class Manga(Livre):
    def __init__(self, titre, auteur, isbn, quantite, editeur, prix, genre):
        super().__init__(titre, auteur, isbn, quantite, editeur, prix)
        self.genre = genre

    def __str__(self):
        return f"{self.titre} par {self.auteur} (Genre: {self.genre})"

# Charger les données depuis le fichier JSON et créer des objets de classe Livre
def charger_base_de_donnees():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            livres = []
            for livre_data in data:
                livre = Livre(livre_data["Titre"], livre_data["Auteur"], livre_data["ISBN"], livre_data["quantité"], livre_data["éditeur"], livre_data["prix"])
                livres.append(livre)
            return livres
    except FileNotFoundError:
        print("Le fichier de base de données n'a pas été trouvé.")
        return []

# Fonction principale pour poser la question et gérer les réponses
def interaction_première(livres):
    print("1. Client")
    print("2. Employer")
    print("3. Quitter le menu")
    choix = input("\nChoisissez une option : 1, 2 ou 3 : ")

    if choix == '1':
        Interaction_client(livres)
    elif choix == '2':
        code = input("Veuillez entrer le code d'accès : ")
        if verif_code(code):
            Interaction_employer(livres)
        else:
            print("\nCode d'accès incorrect.")
            interaction_première(livres)
    elif choix == '3':
        print("\n Vous avez quitté le menu. \n")
    else:
        print("\nOption invalide. Veuillez choisir une option valide : 1, 2 ou 3 : ")
        interaction_première(livres)

# Fonction pour verif code employer
def verif_code(code):
    code_ok = 'mama'
    return code == code_ok

# Définition des fonctions pour chaque option de réponse
def Interaction_client(livres):
    print("\nVous avez choisi l'option Client.")
    rechercher_livre(livres)

def Interaction_employer(livres):
    print("\nVous avez choisi l'option Employer.")
    print("1. Rechercher un livre")
    print("2. Encaisser un livre")
    print("3. Ajouter un livre au stock")
    print("4. Modifier un livre du stock")
    print("5. Supprimer un livre du stock")
    print("6. Quitter le menu\n")
    choix = input("Choisissez une option : 1, 2, 3, 4, 5 ou 6 : ")

    if choix == '1':
        rechercher_livre(livres)
    elif choix == '2':
        encaisser_livre(livres)
    elif choix == '3':
        ajouter_livre(livres)
    elif choix == '4':
        modifier_livre(livres)
    elif choix == '5':
        supprimer_livre(livres)
    elif choix == '6':
        print("\nVous avez quitté le menu.\n")
    else:
        print("Option invalide. Veuillez choisir une option valide : 1, 2, 3, 4, 5 ou 6 : ")
        Interaction_employer(livres)

#                   1. RECHERCHER UN LIVRE
# Interaction pour rechercher un livre
def rechercher_livre(livres):
    print("\nRecherche de livre :")
    critere_recherche = input("Entrez le titre, l'auteur, l'ISBN ou l'éditeur du livre que vous recherchez : ").strip().lower()

    # Créer une liste pour stocker les résultats de la recherche
    resultats = []

    # Parcourir chaque livre dans la liste pour vérifier les critères de recherche
    for livre in livres:
        if critere_recherche in livre.titre.lower() \
                or critere_recherche in livre.auteur.lower() \
                or critere_recherche in livre.isbn.lower() \
                or critere_recherche in livre.editeur.lower():
            resultats.append(livre)

    # Afficher les résultats de la recherche
    if resultats:
        print("\n Résultats de la recherche :")
        for livre in resultats:
            print(f"\nTitre: {livre.titre}")
            print(f"Auteur: {livre.auteur}")
            print(f"ISBN: {livre.isbn}")
            print(f"Quantité: {livre.quantite}")
            print(f"Éditeur: {livre.editeur}")
            print(f"Prix: {livre.prix}€\n")
    else:
        print("\nAucun livre trouvé correspondant à votre recherche.\n")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            rechercher_livre(livres)
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")
        
    return resultats

#                   2. ENCAISSER UN LIVRE
# Fonction pour rechercher un livre par titre
def rechercher_livre_par_titre(titre_recherche, livres):
    for livre in livres:
        if titre_recherche.lower() in livre.titre.lower():
            return livre
    return None

# Interaction pour encaisser un livre
def encaisser_livre(livres):
    print("\nEncaissement d'un livre :")
    titre = input("Entrez le titre du livre à encaisser : ")

    livre = rechercher_livre_par_titre(titre, livres)

    if livre:
        print(f"\n\nEst-ce bien ce livre que vous voulez encaisser ? {livre}")
        print("1. Oui")
        print("2. Non")
        print("3. Quitter le menu")

        choix = input("Choisissez une option : 1, 2 ou 3 : ")
        if choix == '1':
            if livre.quantite > 0:
                livre.quantite -= 1
                print(f"\nUn exemplaire de '{livre.titre}' a été encaissé. Nouvelle quantité : {livre.quantite}")
                print(f"\nPrix à payer pour ce livre : '{livre.prix}€")
                if livre.quantite == 0:
                    print("\nAttention : Ce livre est maintenant Sold Out.\n")
            else:
                print("\nDésolé, ce livre est déjà Sold Out.\n")
        elif choix == '2':
            encaisser_livre(livres)
        elif choix == '3':
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide. Veuillez recommencer.\n")
            encaisser_livre(livres)
    else:
        print(f"Le livre avec le titre '{titre}' n'a pas été trouvé dans la base de données.")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            encaisser_livre(livres)
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")

#                       3. AJOUTER UN LIVRE
# Fonction pour rechercher un livre par ISBN sur Open Library
def recherche_isbn():
    isbn = input("Veuillez entrer un numéro ISBN : ")

    url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    data = response.json()

    if f"ISBN:{isbn}" in data:
        # Extraire les informations nécessaires du résultat de l'API
        livre_info = data[f"ISBN:{isbn}"]
        title = livre_info['title']
        authors = livre_info['authors'][0]['name'] if 'authors' in livre_info else 'Inconnu'
        publish_date = livre_info['publish_date'] if 'publish_date' in livre_info else 'Inconnue'
        publishers = livre_info['publishers'][0]['name'] if 'publishers' in livre_info else 'Inconnu'

        # Demander à l'utilisateur de saisir la quantité et le prix
        quantity = int(input(f"Quantité en stock pour {title} : "))
        price = float(input(f"Prix unitaire (en €) pour {title} : "))

        return title, authors, publish_date, publishers, isbn, quantity, price
    else:
        print("Aucune information trouvée pour cet ISBN.")

# Fonction pour ajouter un livre
def ajouter_livre():
    print("Voulez-vous ajouter un livre manuellement ou depuis une recherche Open Library ?")
    print("1. Manuellement")
    print("2. Depuis une recherche Open Library")
    choix = input("Veuillez choisir une option : 1 ou 2 : ")

    if choix == '1':
        print("Ajout d'un nouveau livre :")
        titre = input("Titre du livre : ")
        auteur = input("Auteur du livre : ")
        isbn = input("ISBN du livre : ")
        quantite = int(input("Quantité disponible : "))
        editeur = input("Éditeur du livre : ")
        prix = float(input("Prix du livre : "))

        try:
            # Charger le contenu du fichier JSON existant
            with open('data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas, initialiser une nouvelle liste
            data = []

        # Ajouter le nouveau livre à la liste existante
        data.append(nouveau_livre.__dict__)

        # Écrire les données mises à jour dans le fichier JSON
        try:
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Livre ajouté avec succès !")
        except Exception as e:
            print("Erreur lors de l'écriture dans le fichier JSON :", e)
        return nouveau_livre

    elif choix == '2':
        # Recherche d'un livre par ISBN sur Open Library
        livre_info = recherche_isbn()

        if livre_info:
            # Création d'un nouvel objet Livre
            nouveau_livre = Livre(*livre_info)
            print("Livre ajouté avec succès !")
            return nouveau_livre

    else:
        print("\nOption invalide\n")

    return None

#                           4. MODIFIER UN LIVRE
def modifier_livre(livres):
    print("Liste des titres des livres :")

    # Afficher la liste des titres des livres
    for livre in livres:
        print(f"Titre: {livre.titre}")

    # Demander à l'utilisateur de choisir le titre du livre à modifier
    titre_livre = input("Entrez le titre du livre à modifier : ")

    # Rechercher le livre par titre
    livre_a_modifier = rechercher_livre_par_titre(titre_livre, livres)

    # Si le livre est trouvé, permettre à l'utilisateur de modifier ses informations
    if livre_a_modifier:
        print(f"Livre trouvé : {livre_a_modifier}")

        # Demander les nouvelles informations à l'utilisateur
        nouveau_titre = input("Entrez le nouveau titre (laissez vide pour ne pas modifier) : ").strip()
        nouveau_auteur = input("Entrez le nouvel auteur (laissez vide pour ne pas modifier) : ").strip()
        nouveau_isbn = input("Entrez le nouvel ISBN (laissez vide pour ne pas modifier) : ").strip()
        nouvelle_quantite = input("Entrez la nouvelle quantité (laissez vide pour ne pas modifier) : ").strip()
        nouveau_editeur = input("Entrez le nouvel éditeur (laissez vide pour ne pas modifier) : ").strip()
        nouveau_prix = input("Entrez le nouveau prix (laissez vide pour ne pas modifier) : ").strip()

        # Mettre à jour les informations du livre si l'utilisateur a fourni de nouvelles valeurs
        if nouveau_titre:
            livre_a_modifier.titre = nouveau_titre
        if nouveau_auteur:
            livre_a_modifier.auteur = nouveau_auteur
        if nouveau_isbn:
            livre_a_modifier.isbn = nouveau_isbn
        if nouvelle_quantite:
            livre_a_modifier.quantite = int(nouvelle_quantite)
        if nouveau_editeur:
            livre_a_modifier.editeur = nouveau_editeur
        if nouveau_prix:
            livre_a_modifier.prix = float(nouveau_prix)

        print("Livre modifié avec succès.")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre_livre}'.")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            modifier_livre(livres)
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")

# Fonction pour supprimer un livre
def supprimer_livre(livres):
    print("Liste des titres des livres :")

    # Afficher la liste des titres des livres
    for livre in livres:
        print(f"Titre: {livre.titre}")

    # Demander à l'utilisateur de choisir le titre du livre à supprimer
    titre_livre = input("Entrez le titre du livre à supprimer : ")

    # Rechercher le livre par titre
    livre_a_supprimer = rechercher_livre_par_titre(titre_livre, livres)

    # Si le livre est trouvé, demander confirmation à l'utilisateur avant de le supprimer
    if livre_a_supprimer:
        print(f"Livre trouvé : {livre_a_supprimer}")
        confirmation = input("Voulez-vous vraiment supprimer ce livre ? (o/n) : ").strip().lower()

        if confirmation == 'o' or confirmation == 'oui':
            # Supprimer le livre de la liste
            livres.remove(livre_a_supprimer)
            print("Livre supprimé avec succès.")
        else:
            print("Suppression annulée.")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre_livre}'.")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            supprimer_livre(livres)
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")

# Appel de la fonction principale pour démarrer l'interaction avec le client
if __name__ == "__main__":
    print("\nBienvenu.e !")
    liste_livres = charger_base_de_donnees()
    interaction_première(liste_livres)