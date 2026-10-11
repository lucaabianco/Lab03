from strumento import Strumento


class DepositoStrumenti:
    lista_strumenti = []
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, "r") as infile:
                for line in infile:
                    fields = line.rstrip('\n').split(",")
                    strumento = Strumento(fields[0], fields[1], fields[2], fields[3], fields[4])
                    self.lista_strumenti.append(strumento)
        except FileNotFoundError:
            print("Errore: file non trovato! Riprova")


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        id = 'S' + str(len(self.lista_strumenti))
        nuovo_strumento = Strumento(id, tipo, marca, anno_acquisto, valore)
        self.lista_strumenti.append(nuovo_strumento)


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.lista_strumenti, key = lambda x : x.marca)

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
