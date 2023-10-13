class Client :
    def _init_(self, adresse, email) :
        self.adresse = adresse
        self.email = email

    def afficher_infos(self) :
        print("Nom:", self.nom)
        print("Adresse:", self.adresse)
        print("Email:", self.email)

    def saisir_nom(self) :
        self.nom = input("Veuillez entrer votre nom : ")


    def identifier(self) :
        self.saisir_nom()

        if self.nom == "AZERTY" :
            print("Identification réussie")
        else :
            print("Identification échouée")


# Création d'une instance de la classe "Client"
client1 = Client()

# Appel de la méthode d'identification
client1.identifier()