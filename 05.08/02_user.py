jmeno = input("Zadejte svoje jmeno")
vek = input("Zadejte svuj vek")
uzivatel = "Jmeno:" + jmeno + '\n' + 'Vek:' + vek

cesta = 'Python/05.08/HW/02_user.txt'

with open(cesta, mode = 'w') as file:
    file.write('Soubor pro udaje uzivatele')

with open(cesta, mode = 'a') as file:
    file.write('\n' + '\n' + uzivatel)
