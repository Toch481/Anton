import re
import requests
from bs4 import BeautifulSoup

# sem zkopírovat ručně URL z okan co vyskočí po spuštění Web_browser.py
result = requests.get("https://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=jdVVQzgiWH6twCrev0i9iaeXTyC7xQDLh5XAqcnLiO_ejGlXaE6MQC2MM55C5YFEDa1wqVW-Z9Ln5TyIKHW9yZ88bdZfv1nGRbQvqY2pUC-olJpAhFnz6-LjZpjkVYca")

src = result.content
# ten parser se tam má dávat jinak to hází error
soup = BeautifulSoup(src, "html.parser")


# tohle si z tý strany vytáhne všechny data a vrátí jen text a používám to v I_know.py
text = soup.get_text()
text1 = " ".join(text.split())
# blok textu z kterýho vycucnu vše potřebný v I_know.py
# print(text1)

# Tahle část je na vlastníky


elems = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(2) > td:nth-child(1)')
# nevim jestli select nebo select one

# když je víc vlastníků tak potřeba hledat i zbytek musim si otestovat jednoho vlastníka a víc a zjistti jestli je to jen ten nth.child
# tady potřebuju to udělat nějak smart asi loop? aby to přidávalo to tr:nth-child(X) +1 +1 +1 dokud to nevrátí prázdný závorky '[]'

# takhle to vypadá když tam je jeden - první v řadě
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(2) > td:nth-child(1)

# takhle to vypadá když tam jsou dva se stejnou adresou - první v řade
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(2) > td:nth-child(1)
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(3) > td:nth-child(1)

# takhle to vypadá když jsou dva a maj jiný adresy (třetí v řadě proto začíná (4))
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(4) > td:nth-child(1)
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(5) > td > i
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(6) > td > i
elems1 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(2) > td:nth-child(1)')
elems2 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(3) > td:nth-child(1)')
elems3 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(4) > td:nth-child(1)')
elems4 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(5) > td > i')

print(elems)
print(elems1)
print(elems2)
print(elems3)
print(elems4)

# Tohle je na způsob ochrany
# tohle to vrátí když nejsou evidovány způsoby ochrany
#content > div:nth-child(10)

# Tohle to vrátí když jsou
#content > table:nth-child(10) > tbody > tr:nth-child(1) > td
#content > table:nth-child(10) > tbody > tr:nth-child(2) > td

elems5 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(5) > td > i')
print(elems5)