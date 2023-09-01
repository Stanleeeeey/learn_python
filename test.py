from exercises import variables

def test(name, excpected_value, tested_code):


    try:
        tested_code = eval(tested_code)
        if tested_code ==  excpected_value: print(f" test {name} powiódł się")
        else: print(f" test {name} nie powiódł się otrzymano wartość {tested_code} a oczekiwano: {excpected_value}")
    except Exception as e:
        print(f"test {name} nie powiódł się z powodu {e}")






test(
    "var1.py",
    True,
    "variables.var1.nowa_zmienna == 7"    
)

test(
    "var2.py",
    True,
    "type(variables.var2.imie) == str and type(variables.var2.wiek) == int "    
)


