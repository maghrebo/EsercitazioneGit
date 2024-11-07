# Inizializzazione della variabile per la somma
somma = 0

# Ciclo che continua finché l'utente non inserisce 0
while True:
    # Chiedi all'utente di inserire un numero
    numero = int(input("Inserisci un numero intero (inserisci 0 per terminare): "))
    
    # Se il numero è 0, termina il ciclo
    if numero == 0:
        break
    
    # Aggiungi il numero alla somma
    somma += numero

# Stampa la somma totale
print(f"La somma di tutti i numeri inseriti è: {somma}")
