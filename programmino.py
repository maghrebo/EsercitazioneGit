
somma = 0

# Ciclo che continua finché non si inserisce 0
while True:
    
    numero = int(input("Inserisci un numero intero (inserisci 0 per terminare): "))
    
    if numero == 0:
        break
    
    somma += numero

print(f"La somma di tutti i numeri inseriti è: {somma}")
