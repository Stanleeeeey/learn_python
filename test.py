from exercises import variables

def test(name, excpected_value, tested_code):


    try:
        tested_code = exec(tested_code)
        if tested_code ==  excpected_value: print(f" test {test.name} powiódł się")
        else: print(f" test {name} nie powiódł się otrzymano wartość {tested_code} a oczekiwano: {excpected_value}")
    except Exception as e:
        print(f"test {name} nie powiódł się z powodu {e}")






test(
    "var1.py",
    7,
    "variables.var1.nowa_zmienna"
        
)



