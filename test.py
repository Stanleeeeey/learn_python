from exercises import variables, lists, elseif

from colorama import Fore, Back, Style





suceed = 0
tested = 0

def test(name, excpected_value, tested_code):
    global tested, suceed

    try:
        tested_code = eval(tested_code)
        if tested_code ==  eval(excpected_value):
            print(Fore.GREEN + f" test {name} powiódł się")
            suceed += 1
        else: print(Fore.RED + f" test {name} nie powiódł się otrzymano wartość {tested_code} a oczekiwano: {excpected_value}")
    except Exception as e:
        print(Fore.RED + f"test {name} nie powiódł się z powodu {e}")

    tested += 1






test(
    "var1.py",
    '7',
    "variables.var1.nowa_zmienna"    
)

test(
    "var2.py",
    "True",
    "type(variables.var2.imie) == str and type(variables.var2.wiek) == int"    
)

test(
    "var3.py",
    "'Alex'",
    "variables.var3.imie"    
)

test(
    "var5.py",
    "variables.var4.skladnik_1 + variables.var4.skladnik_2",
    "variables.var4.suma"    
)

test(
    "var4.py",
    "'7'",
    "variables.var5.zmienna1"    
)

test(
    "var6.py",
    "4//3",
    "variables.var6.wynik"    
)

test(
    "var7.py",
    "12345678910 % 1234",
    "variables.var7.reszta"    
)

test(
    "var8.py",
    "3**10",
    "variables.var8.wynik"    
)


test(
    "var9.py",
    "'hello world'",
    "variables.var9.hello_world"    
)

test(
    "list1.py",
    "42",
    "lists.list1.lista[0]"    
)

test(
    "if1.py",
    "False",
    "elseif.if1.czy_podzielna"    
)

test(
    "if2.py",
    "True",
    "sum([1 if elseif.if2.czy_parzysta(x) == (x%2 == 0) else 0 for x in range(1000)]) == 1000"    
)

def if3(x):
    return x>=16

test(
    "if3.py",
    "True",
    "sum([True if elseif.if3.czy_moze_ogladac_oppenheimera(x) ==if3(x) else False for x in range(100)]) == 100"    
)

def if4(x): #nie przejmuj się tym
    miejsce_zamieszkania = None
    #masz do dyspozycji znak x będący pierwszym znakiem peselu użyj tylko jednego if (ilosc else i elif nie ograniczona)
    #pisz pod tym
    
    if 0 == x:
        miejsce_zamieszkania = "Nowy Bajt"
    elif 1 == x: miejsce_zamieszkania = "Baiszawa"
    elif 2 == x: miejsce_zamieszkania = "wioska"
    else: miejsce_zamieszkania = "zły pesel"
    

    #dotąd
    return miejsce_zamieszkania

test(
    "if4.py",
    "True",
    "sum([True if elseif.if4.sprawdzarka(x) ==if4(x) else False for x in range(10)]) == 10"    
)

print(Fore.WHITE + f"przeprowadzono {tested} testów z procentem udanych {suceed / tested *100}%")

