class Prestito:
    def __init__(self,id_prestito, id_strumento, cognome_allievo, data):
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo
        self.data = data
        self.id_prestito = id_prestito

    def __str__(self):
        return f"{self.id_prestito} {self.id_strumento} {self.cognome_allievo} {self.data}"