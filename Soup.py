import re
import requests
from bs4 import BeautifulSoup

# sem zkopírovat ručně URL z okan co vyskočí po spuštění Web_browser.py
result = requests.get("https://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=BDOdwKjzl4IzlysRdicDwIp70n6G1VKk3YULLPSc_Po4Pj0To0rHc47naTmfl_la4oLnPTvZZsZBHLmSTtkdoOdH7qkgNKEpu7NjbLSBfEdeSjKhXzZZiWAfd7x_z9tQ")

print(result.status_code)

src = result.content
soup = BeautifulSoup(src, "html.parser")
links = soup.find_all("td")

# tohle si z tý strany vytáhne všechny data a vrátí jen text
text = soup.get_text()
text1 = " ".join(text.split())
print(text1)
print("_" * 10)
# tohle hledá ty data co budu potřebovat a vrátí mi to číslo pozice prvního písmena ve stringu
print(text1.find("Parcelní číslo:"), text1.find("Katastrální území:"), text1.find("[Číslo LV:]"), )
obec = text1.find("Obec:")
# funguje ale hrozná prasárna ^^
print(text1[315+5],text1[315+6],text1[315+7],text1[315+8],text1[315+9],text1[315+10])




