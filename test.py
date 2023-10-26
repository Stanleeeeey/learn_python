from exercises import variables, lists, elseif, loops, slowniki, functions, classes
import sys
import random

try:
    from colorama import Fore
except:
    class Fore:
        GREEN = ""
        RED = ""
        WHITE = ""

try:
    cont = not (sys.argv[1] == "cont")
except:
    cont = True

suceed = 0
tested = 0

def test(name, excpected_value, tested_code):
    global tested, suceed

    try:
        tested_code = eval(tested_code)
        if tested_code ==  eval(excpected_value):
            print(Fore.GREEN + f" test {name} powiodł sie")
            suceed += 1
        else: print(Fore.RED + f" test {name} nie powiodl się otrzymano wartosc {tested_code} a oczekiwano: {excpected_value}")
    except Exception as e:
        print(Fore.RED + f"test {name} nie powiodl sie z powodu {e}")
        if not cont:
            print(Fore.WHITE + "konczymy sprawdzac")
            exit(0)

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
    "var4.py",
    "variables.var4.skladnik_1 + variables.var4.skladnik_2",
    "variables.var4.suma"    
)

test(
    "var5.py",
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
    "list2.py",
    "len(lists.list2.lista)",
    "lists.list2.dlugosc"    
)

test(
    "list3.py",
    "42",
    "lists.list3.lista[-1]"    
)

test(
    "list4.py",
    "lists.list4.lista.index(42)",
    "lists.list4.index"    
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

def if5(x):
    if x %2 == 0 and x%3 == 0: return 6
    else:return 1

test(
    "if5.py",
    "True",
    "sum([True if elseif.if5.sprawdzarka(x) ==if5(x) else False for x in range(10)]) == 10"    
)

test(
    "loop1.py",
    "sum(loops.loop1.lista)",
    "loops.loop1.suma"    
)

test(
    "loop2.py",
    '''["GOSSIP", "SUPERMODEL", "OWN MY MIND", "MAMMAMIA", "LA FINE", "KOOL KIDS", "TIMEZONE", "GASOLINE", "THE LONELIEST", "DON'T WANNA SLEEP"]''',
    "loops.loop2.piosenki"    
)

test(
    "loop3.py",
    '"".join(["hej" for i in range(10)])',
    "loops.loop3.wynik"    
)

test(
    "loop4.py",
    '"0123456789"',
    "loops.loop4.wynik"    
)

test(
    "dict1.py",
    "('Alan', 32)",
    "(slowniki.dict1.czlowiek['imie'], slowniki.dict1.czlowiek['wiek'])"

)

test(
    "dict2.py",
    "'Alan'",
    "slowniki.dict2.czlowiek['imie']"

)

test(
    "fun1.py",
    "1000",
    "sum([ i+2 == functions.fun1.zwieksz(i) for i in range(1000) ])"

)


def zwieksz(x, y = 2):
    return x+y


test(
    "fun2.py",
    "(10000, 1000)",
    "(sum([sum([zwieksz(x, y) == functions.fun2.zwieksz(x, y) for x in range(100) ]) for y in range(100)]), sum([ i+2 == functions.fun2.zwieksz(i) for i in range(1000) ]))"

)

def fib1(x):
    previous = 1
    current = 1
    nexti = 0
    for i in range(x-2):
        nexti = current + previous
        previous = current
        current = nexti

    return current

test(
    "fun3.py",
    "100",
    "sum([ fib1(i) == functions.fun3.fibonaci(i) for i in range(100) ])"

)

test(
    "fun4.py",
    "100",
    "sum([ fib1(i) == functions.fun4.fibonaci(i) for i in range(100) ])"

)

def dot(x,y):
    suma = 0
    for i in range(len(x)):
        suma += x[i] *y[i]

    return suma


test(
    "fun5.py",
    "dot([31,20,16], [42,51,6689])",
    "functions.fun5.dot([31,20,16], [42,51,6689])"

)


def factorial(x):
    res = 1
    for i in range(1, x+1):
        res*= i
    return res

test(
    "fun6.py",
    "100",
    "sum([factorial(i) == functions.fun6.silnia(i) for i in range(100)])"

)

test(
    "fun7.py",
    "100",
    "sum([factorial(i) == functions.fun7.silnia(i) for i in range(100)])"

)


commands = [
    "",
    "heal",
    "hit",
    "safe"
]

def npcControll(command, npc):
    if command == "":
        if npc["position"][0] > 100:

            npc["position"][0] -= npc["speed"]
        else:
            npc["position"][0] += npc["speed"]
    elif command == "heal":
        npc["health"] = min(100, npc["health"])
    elif command == "hit":
        npc["speed"] *= 2
        npc["health"] -= 10
        npc["position"][1] += npc["speed"]
    elif command == "safe":
        npc["speed"] /= 2
    
def generateNPC():
    return {
        "name": "grzegorz",
        "health": random.randint(1,100),
        "speed": 2*random.randint(1,10),
        "position": [random.randint(1,100), random.randint(1,100)]
    }

test(
    "fun8.py",
    "100",
    "sum([npcControll(*i) == functions.fun8.AI(*i) for i in [(random.choice(commands), generateNPC()) for j in range(100)]])"

)

test(
    "class1.py",
    "'Max'",
    "classes.class1.Czlowiek().imie"

)

def check_class2():
    human = classes.class2.Czlowiek()
    human.zmien_wiek(20)
    return human.wiek

test(
    "class2.py",
    "20",
    '''check_class2()'''

)


def check_class3():
    human = classes.class3.Czlowiek()
    human.inicjalizuj("Max", 20)
    return human.imie, human.wiek

test(
    "class3.py",
    "('Max', 20)",
    '''check_class3()'''

)

def check_class4():
    human = classes.class4.Czlowiek("Max", 20)
    
    return human.imie, human.wiek

test(
    "class4.py",
    "('Max', 20)",
    '''check_class4()'''

)


def check_class5():
    cat = classes.class5.Cat("Max", 20)
    
    return cat.make_noise()


test(
    "class5.py",
    "'miau'",
    '''check_class5()'''

)

def check_class4():
    human = classes.class6.Jaskolka("Max", 20, 'european')
    
    return human.name, human.age, human.gatunek

test(
    "class4.py",
    "('Max', 20, 'european')",
    '''check_class4()'''

)

print(Fore.WHITE + f"przeprowadzono {tested} testów z procentem udanych {suceed / tested *100}%")

