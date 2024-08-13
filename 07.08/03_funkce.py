heslo = input('Zadejte prosím heslo, které má alespoň 5 znaků: ')

def test_heslo(heslo: str):
    return len(heslo) >= 5

if test_heslo(heslo):
    print("Heslo je v pořádku.")
else:
    print("Heslo musí mít alespoň 5 znaků.")