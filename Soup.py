import re
import requests
from bs4 import BeautifulSoup

# sem zkopírovat ručně URL z okan co vyskočí po spuštění Web_browser.py
result = requests.get("https://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=RZeR1DVPOWBz_SPkP9spu7jMEXzF9-Z3GvCakI9bDEnAuZfln1wLQmxeqEaMQeWnWeEac2f5NkBC1oHHvQfR7zRD-x_ozX958X9VwF6HanIVwK2F6w9376fRAocihE3E")

src = result.content
# ten parser se tam má dávat jinak to hází error
soup = BeautifulSoup(src, "html.parser")


# tohle si z tý strany vytáhne všechny data a vrátí jen text a používám to v I_know.py
text = soup.get_text()
text1 = " ".join(text.split())
# blok textu z kterýho vycucnu vše potřebný v I_know.py
print(text1)

# Tahle část je na vlastníky

#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(2) > td:nth-child(1)
elems = soup.select_one('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(2) > td:nth-child(1)')
# nevim jestli select nebo select one

# když je víc vlastníků tak potřeba hledat i zbytek musim si otestovat jednoho vlastníka a víc a zjistti jestli je to jen ten nth.child
# tady potřebuju to udělat nějak smart asi loop? aby to přidávalo to tr:nth-child(X) +1 +1 +1 dokud to nevrátí prázdný závorky '[]'
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(3) > td > i
elems1 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(3) > td > i')
#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(4) > td > i
elems2 = soup.select('#content > table.zarovnat.stinuj.zarovnat.stinuj.vlastnici > tbody > tr:nth-child(4) > td > i')


print(elems)
print(elems1)
print(elems2)


