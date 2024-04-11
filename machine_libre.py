import requests
import json

###                                  LES CLASSES 

# Définition de la classe parent "Livre"
class Livre:
    def __init__(self, titre, auteur, isbn, quantite, editeur, prix, type):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.quantite = quantite
        self.editeur = editeur
        self.prix = prix
        self.type = type

    def __str__(self):
        return f"{self.titre} par {self.auteur}"
# Définition de la classe enfant "Manga" qui hérite de la classe "Livre"
class Manga(Livre):
    def __init__(self, titre, auteur, isbn, quantite, editeur, prix, genre, type):
        super().__init__(titre, auteur, isbn, quantite, editeur, prix, type)
        self.genre = genre

    def __str__(self):
        return f"{self.titre} par {self.auteur} (Genre: {self.genre})"




###                               GESTION DE BD
def charger_base_de_donnees():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
            livres_et_mangas = []
            for item_data in data:
                if item_data["type"] == "manga":
                    manga = Manga(item_data["titre"], item_data["auteur"], item_data["isbn"], item_data["quantite"], item_data["editeur"], item_data["prix"], item_data["genre"], item_data["type"])
                    livres_et_mangas.append(manga)
                else:  # Sinon, c'est un livre
                    livre = Livre(item_data["titre"], item_data["auteur"], item_data["isbn"], item_data["quantite"], item_data["editeur"], item_data["prix"], item_data["type"])
                    livres_et_mangas.append(livre)
            return livres_et_mangas
    except FileNotFoundError:
        print("Le fichier de base de données n'a pas été trouvé.")
        return []

def sauvegarder_base_de_donnees(livres_et_mangas):
    try:
        with open('data.json', 'w') as f:
            # Convertir les objets Livre et Manga en dictionnaires pour la sérialisation JSON
            livres_et_mangas_data = []
            for item in livres_et_mangas:
                item_data = item.__dict__
                if isinstance(item, Manga):
                    item_data["type"] = "manga"
                else:
                    item_data["type"] = "livre"
                livres_et_mangas_data.append(item_data)
            json.dump(livres_et_mangas_data, f, indent=4)
            print("Données mises à jour sauvegardées avec succès.")
    except Exception as e:
        print("Erreur lors de l'écriture dans le fichier JSON :", e)


###                              GESTION DES INTERACTIONS
# Fonction principale pour poser la question et gérer les réponses
def interaction_première(livres_et_mangas):
    print("1. Client")
    print("2. Employer")
    print("3. Quitter le menu")
    choix = input("\nChoisissez une option : 1, 2 ou 3 : ")

    if choix == '1':
        Interaction_client(livres_et_mangas)
    elif choix == '2':
        print("\nVous avez choisi l'option Employer.")
        code = input("Veuillez entrer le code d'accès : ")
        if verif_code(code):
            Interaction_employer(livres_et_mangas)
        else:
            print("\nCode d'accès incorrect.")
            interaction_première(livres_et_mangas)
    elif choix == '3':
        print("\n Vous avez quitté le menu. \n")
    else:
        print("\nOption invalide. Veuillez choisir une option valide : 1, 2 ou 3 : ")
        interaction_première(livres_et_mangas)

# Fonction pour verif code employer
def verif_code(code):
    code_ok = 'mama'
    return code == code_ok

# Définition des fonctions pour chaque option de réponse
def Interaction_client(livres_et_mangas):
    print("\nVous avez choisi l'option Client.")
    rechercher_livre(livres_et_mangas)

def Interaction_employer(livres_et_mangas):
    print("1. Rechercher un livre")
    print("2. Encaisser un livre")
    print("3. Ajouter un livre au stock")
    print("4. Modifier un livre du stock")
    print("5. Supprimer un livre du stock")
    print("6. Quitter le menu\n")
    choix = input("Choisissez une option : 1, 2, 3, 4, 5 ou 6 : ")

    if choix == '1':
        rechercher_livre(livres_et_mangas)
    elif choix == '2':
        encaisser_livre(livres_et_mangas)
    elif choix == '3':
        ajouter_livre(livres_et_mangas)
    elif choix == '4':
        modifier_livre(livres_et_mangas)
    elif choix == '5':
        supprimer_livre(livres_et_mangas)
    elif choix == '6':
        print("\nVous avez quitté le menu.\n")
    else:
        print("Option invalide. Veuillez choisir une option valide : 1, 2, 3, 4, 5 ou 6 : ")
        Interaction_employer(livres_et_mangas)




###                           1. RECHERCHER UN LIVRE
# Interaction pour rechercher un livre
def rechercher_livre(livres_et_mangas):
    print("\nRecherche de livre :")
    critere_recherche = input("Entrez le titre, l'auteur, l'ISBN ou l'éditeur du livre ou manga que vous recherchez : ").strip().lower()

    # Créer une liste pour stocker les résultats de la recherche
    resultats = []

    # Parcourir chaque livre ou manga dans la liste pour vérifier les critères de recherche
    for livre in livres_et_mangas:
        if critere_recherche in livre.titre.lower() \
                or critere_recherche in livre.auteur.lower() \
                or critere_recherche in livre.isbn.lower() \
                or critere_recherche in livre.editeur.lower():
            resultats.append(livre)

    # Afficher les résultats de la recherche
    if resultats:
        print("\nRésultats de la recherche :")
        for livre in resultats:
            print(f"\nTitre: {livre.titre}")
            print(f"Auteur: {livre.auteur}")
            print(f"ISBN: {livre.isbn}")
            print(f"Quantité: {livre.quantite}")
            print(f"Éditeur: {livre.editeur}")
            print(f"Prix: {livre.prix}€")
            print(f"Type: {livre.type}")
            # Vérifier si l'objet est un manga et afficher son genre
            if isinstance(livre, Manga):
                print(f"Genre: {livre.genre}\n")
            else:
                print("")

    else:
        print("\nAucun livre/manga trouvé correspondant à votre recherche.\n")
        print("\n1. Effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            rechercher_livre(livres_et_mangas)
        elif choix == '2':
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")

    return resultats




###                                 2. ENCAISSER UN LIVRE
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
                # Sauvegarder les données mises à jour dans le fichier JSON
                sauvegarder_base_de_donnees(livres)
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



###                                 3. AJOUTER UN LIVRE
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
        publishers = livre_info['publishers'][0]['name'] if 'publishers' in livre_info else 'Inconnu'
        # Demander à l'utilisateur de saisir la quantité et le prix
        quantity = int(input(f"Quantité en stock pour {title} : "))
        price = float(input(f"Prix unitaire (en €) pour {title} : "))
        type = "livre"

        return title, authors, isbn, quantity, publishers, price, type
    else:
        print("Aucune information trouvée pour cet ISBN.")

# Fonction pour ajouter un livre
def ajouter_livre(livres_et_mangas):
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

        # Créer un nouvel objet Livre
        nouveau_livre = Livre(titre, auteur, isbn, quantite, editeur, prix, "livre")
        # Ajouter le nouveau livre à la liste des livres et mangas
        livres_et_mangas.append(nouveau_livre)
        # Sauvegarder les données mises à jour dans le fichier JSON
        sauvegarder_base_de_donnees(livres_et_mangas)
        print("Livre modifié avec succès.")
        return nouveau_livre

    elif choix == '2':
        # Recherche d'un livre par ISBN sur Open Library
        livre_info = recherche_isbn()

        if livre_info:
            # Création d'un nouvel objet Livre
            nouveau_livre = Livre(*livre_info)
            # Ajouter le nouveau livre à la liste des livres et mangas
            livres_et_mangas.append(nouveau_livre)
            # Sauvegarder les données mises à jour dans le fichier JSON
            sauvegarder_base_de_donnees(livres_et_mangas)
            print("Livre ajouté avec succès !")
            return nouveau_livre
    else:
        print("\nOption invalide\n")

    return None
## 4. MODIFIER UN LIVRE
def modifier_livre(livres_et_mangas):
    print("Liste des titres des livres :")

    # Afficher la liste des titres des livres
    for livre in livres_et_mangas:
        print(f"Titre: {livre.titre}")

    # Demander à l'utilisateur de choisir le titre du livre à modifier
    titre_livre = input("Entrez le titre du livre à modifier : ")

    # Rechercher le livre par titre
    livre_a_modifier = rechercher_livre_par_titre(titre_livre, livres_et_mangas)

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
        # Sauvegarder les données mises à jour dans le fichier JSON
        sauvegarder_base_de_donnees(livres_et_mangas)
        print("Livre modifié avec succès.")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre_livre}'.")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            modifier_livre(livres_et_mangas)
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")



###                                      5. SUPPRIMER UN LIVRE
# Fonction pour supprimer un livre
def supprimer_livre(livres_et_mangas):
    print("Liste des titres des livres :")

    # Afficher la liste des titres des livres
    for livre in livres_et_mangas:
        print(f"Titre: {livre.titre}")

    # Demander à l'utilisateur de choisir le titre du livre à supprimer
    titre_livre = input("Entrez le titre du livre à supprimer : ")

    # Rechercher le livre par titre
    livre_a_supprimer = None
    for livre in livres_et_mangas:
        if livre.titre.lower() == titre_livre.strip().lower()
            livre_a_supprimer = livre
            break

    # Si le livre est trouvé, demander confirmation à l'utilisateur avant de le supprimer
    if livre_a_supprimer:
        print(f"Livre trouvé : {livre_a_supprimer.titre}")
        confirmation = input("Voulez-vous vraiment supprimer ce livre ? (o/n) : ").strip().lower()

        if confirmation == 'o' or confirmation == 'oui':
            # Supprimer le livre de la liste
            livres_et_mangas.remove(livre_a_supprimer)
            # Enregistrer les modifications dans le fichier JSON
            sauvegarder_base_de_donnees(livres_et_mangas)
            print("Livre supprimé avec succès.")
        else:
            print("Suppression annulée.")
    else:
        print(f"Aucun livre trouvé avec le titre '{titre_livre}'.")
        print("\n1. effectuer une autre recherche.")
        print("2. Quitter le menu.\n")
        choix = input("Veuillez choisir une option : 1 ou 2 : ")
        if choix == '1':
            supprimer_livre(livres_et_mangas)
        elif choix == '2' :
            print("\nVous avez quitté le menu.\n")
        else:
            print("\nOption invalide\n")



###              FONCTION PRINCIPALE
if __name__ == "__main__":
    print("\nBienvenu.e !")
    liste_livres = charger_base_de_donnees()
    interaction_première(liste_livres)