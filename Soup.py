import re
import requests
from bs4 import BeautifulSoup

# sem zkopírovat ručně URL z okan co vyskočí po spuštění Web_browser.py
result = requests.get("https://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=-USHQr2uYOJwz1pUm9K3cMmyRwQ7tH412tHip-y-qDdPFTx3yqx-cZESauRa6pYsj-_f0jH0M-oBVhntaW6xnGqYqp7bPIo6BannR6sd6ZxCli5K1S5EppQpDMhJ79t6")

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




