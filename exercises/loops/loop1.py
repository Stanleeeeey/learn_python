# jako zapalony matematyk chcesz wyliczyc sume listy ponizej

# wynik zapisz do zmiennej suma, dla odważnych dodaj tylko jedną linijkę
lista = [1,2,3,3,4,4,5,5,56,6,6,6,6,67,7,7,8,8,9,9]
suma = 0
for element in lista:
    suma = suma + element

suma = 0
for i in range(len(lista)):
    suma = suma + lista[i]

suma = sum(lista)