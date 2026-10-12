from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.lista_strumenti = []
        self.lista_prestiti = list()
        self.contatore_prestiti = 0

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, "r") as infile:
                for line in infile:
                    fields = line.rstrip('\n').split(",")
                    strumento = Strumento(fields[0], fields[1], fields[2], fields[3], fields[4])
                    self.lista_strumenti.append(strumento)
        except FileNotFoundError:
            raise FileNotFoundError("Errore: file non trovato! Riprova")


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        if not self.lista_strumenti:
            id = 'S1'
        else:
            id = 'S' + str(int(self.lista_strumenti[-1].id[1:]) + 1)
        nuovo_strumento = Strumento(id, tipo, marca, anno_acquisto, valore)
        self.lista_strumenti.append(nuovo_strumento)
        return nuovo_strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.lista_strumenti, key = lambda x : x.marca)


    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        ok = False
        for strumento in self.lista_strumenti:
            if id_strumento == strumento.id:
                ok = True
                break
        if not ok:
            raise Exception("Errore: lo strumento non esiste")

        for prestito in self.lista_prestiti:
            if id_strumento == prestito.id_strumento:
                raise Exception("Errore: strumento non disponibile")

        self.contatore_prestiti += 1
        id_prestito = 'P' + str(self.contatore_prestiti)
        prestito = Prestito(id_prestito, id_strumento, cognome_allievo, data)
        self.lista_prestiti.append(prestito)
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for prestito in self.lista_prestiti:
            if id_prestito == prestito.id_prestito:
                self.lista_prestiti.remove(prestito)
                return
        raise Exception("Errore: prestito non trovato")