import json
import machine_libre

if __name__ == "__main__":
    print("\nBienvenu.e !")
    liste_livres = machine_libre.charger_base_de_donnees()
    machine_libre.rechercher_livre(liste_livres)