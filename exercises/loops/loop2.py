# jako fan albumu RUSH zespołu maneskin nie mozesz patrzec jak ktos zapisal do listy nazwy piosenek malymi literami (oryginalnie nazwy pisoenek z tego albumu sa pisane tylko z uzyciem duzych liter) napraw to, wynik zapisz w takiej kolejnosci w zmiennej piosenki!!

#nie modyfikuj linijki ponizej i tak to nie jest caly album
piosenki = ["gossip", "supermodel", "own my mind", "mammamia", "la fine", "kool kids", "timezone", "gasoline", "the loneliest", "don't wanna sleep"]
piosenki2 = []
for piosenka in piosenki:
    piosenki2.append(piosenka.upper())

piosenki = piosenki2


for i in range(len(piosenki)):
    piosenki[i] = piosenki[i].upper()

