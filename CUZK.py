import requests
from bs4 import BeautifulSoup

result = requests.get("https://nahlizenidokn.cuzk.cz/VyberParcelu.aspx")

print(result.status_code)

src = result.content
soup = BeautifulSoup(src,("html.parser"))
links = soup.find_all("input")
print(links)
print("\n")

# for link in links:
#      if "Zeměměřický úřad" in link.text:
#         print(link)
#         print(link.attrs['href'])