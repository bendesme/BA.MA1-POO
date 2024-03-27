"""
def search_article_by_isbn(self):
	isbn = input("Veuillez entrer un numéro ISBN : ")

	url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"

	response = requests.get(url)
	data = response.json()

		# Extraire les informations nécessaires du résultat de l'API
	title = data[f"ISBN:{isbn}"]['title']
	author = data[f"ISBN:{isbn}"]['authors'][0]['name']
	year=data[f"ISBN:{isbn}"]['publish_date']
	maison_ed=data[f"ISBN:{isbn}"]['publishers'][0]["name"]

		# Demander à l'utilisateur de saisir la quantité et le prix
	quantity = int(input(f"Quantité en stock pour {title} : "))
	price = float(input(f"Prix unitaire (en €) pour {title} : "))
	articlenouv=Livre(isbn,title,price,author,maison_ed,year,None,"ND",isbn,quantity,None)

		# Ajouter l'article au stock
	self.articlesList.append(articlenouv)
	print(f"Article ajouté de OpenLibrary : {title} de {author}")
"""