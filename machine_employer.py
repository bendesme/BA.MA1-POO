import json
import machine_libre
import requests


if __name__ == "__main__":
    print("\nBienvenu.e !")
    liste_livres = machine_libre.charger_base_de_donnees()
    machine_libre.Interaction_employer(liste_livres)