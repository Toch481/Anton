import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\jiric\\Downloads\\P_test\\chromedriver.exe')
# nactení katastru
browser.get("https://nahlizenidokn.cuzk.cz/VyberParcelu.aspx")

# najde políčko na vyplnění kat. uzemí
kat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_vyberObecKU_vyberKU_txtKU")

# pošle tam hledaný uzemí, zatím natvrdo pouději z měnit nebo navázat na input podle zakázky
kat.send_keys("Turnov")
# najde potvrzovací tlačítko a klickne
kat_vyhledat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_vyberObecKU_vyberKU_btnKU")
kat_vyhledat.click()
# najde okno na číslo pzemku před lomítkem
parcela_pred = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_txtParcis")
# pošle tam hledanou parcelu, zatím natvrdo časem první podle inputu a zbytek bude projíždět podle sousedů
parcela_pred.send_keys("2773")

# najde okno na číslo pzemku po lomítku (šlo by nahradit zmáčknutím tabu)
parcela_po = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_txtParpod")
parcela_po.send_keys("1")

# to samý jako nad tímhle akorda za lomítkem
parcela_vyhledat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_btnVyhledat")
# najde potvrzovací tlačítko a klickne
parcela_vyhledat.click()

# print(browser.current_url)
result = requests.get(browser.current_url) #

print(result.status_code)

src = result.content
soup = BeautifulSoup(src,("html.parser"))
links = soup.find_all("td")
print(links)

#print("\n")

# for link in links:
#     if "Vše" in link.text:
#         print(link)
#         print(link.attrs['href'])