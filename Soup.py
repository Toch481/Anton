import requests
from bs4 import BeautifulSoup

result = requests.get("https://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=V7QuMFUF6y34Poam58q3DsdBtycvMWXJJEMehp6v-I-efAIKNzIq3AWq4nxEYO9oW46NG5cdW8oY4v0g1FcYUvILvMQbwEuNtgB_mXU6gJb-zHb4dhWApHYxNuNLy6QU")

print(result.status_code)

src = result.content
soup = BeautifulSoup(src, "html.parser")
links = soup.find_all("td")

# print(links)
text = soup.get_text()
text1 = " ".join(text.split())
print(text1)
print("_" * 10)
print(text1.find("Parcelní číslo:"), text1.find("Obec:"), text1.find("Katastrální území:"), text1.find("[Číslo LV:]"), )
print(text1[315+5],text1[315+6],text1[315+7],text1[315+8],text1[315+9],text1[315+10])
