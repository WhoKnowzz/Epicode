import math

print("Benvenuto! Questo programma ti permette di calcolare il perimetro di diverse figure geometriche\n")

while True:
	print("Scegli la figura geometrica o inserisci 0 per uscire dal programma:\n0) Esci dal programma\n1) Quadrato\n2) Cerchio\n3) Rettangolo\n4) Triangolo\n")
	print("conosci il numero preferito dei 'Waldos'?? cercalo!:V\n")
	scelta = input()

	if scelta == "0":
	    break

	elif scelta == "1":
	    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
	    perimetro = lato * 4
	    print(f"Il perimetro del quadrato è: {perimetro} il\n")

	elif scelta == "2":
	    raggio = float(input("Inserisci il raggio del cerchio: "))
	    circonferenza = 2 * math.pi * raggio
	    print(f"La circonferenza del cerchio è: {circonferenza} num\n")

	elif scelta == "3":
	    base = float(input("Inserisci la base del rettangolo: "))
	    altezza = float(input("Inserisci l'altezza del rettangolo: "))
	    perimetro = (base + altezza) * 2
	    print(f"Il perimetro del rettangolo è: {perimetro} è\n")

	elif scelta == "4":
	    lato1= float( input (" Inserisci il lato AB del triangolo: "))
	    lato2= float( input (" Inserisci il lato BC del triangolo: "))
	    lato3= float( input (" Inserisci il lato AC del triangolo: "))
	    perimetro = lato1+lato2+lato3
	    print(f" Il perimetro del triangolo è: {perimetro}\n")
	    print("4 e venti senza congiunzione\n")
	elif scelta == "420":
	    print("\nQuesto è un piccolo easter egg,se mi hai trovato,hai qualcosa da dirmi!<===SS\n")
	    print("\nSpero sia stato divertente!!Ciao!!\n")
	    break
else:
	print("Scelta non valida. Riprova selezionando una figura corretta.\n")
