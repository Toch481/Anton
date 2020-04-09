import requests
from bs4 import BeautifulSoup


def get_parcel(url):
	result = requests.get(url)
	if result.status_code != 200:
		print(f"Request returned undesired status code: {result.status_code}")
		return
	return result.content


def soup_find(searchstring):
	links = BeautifulSoup(get_parcel(
		url="https://nahlizenidokn.cuzk.cz/VyberParcelu.aspx"),
		"html.parser"
	).find_all(searchstring)
	return links


print(f"{soup_find(searchstring='input')} \n")

# for link in links:
#      if "Zeměměřický úřad" in link.text:
#         print(link)
#         print(link.attrs['href'])