import requests
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\jiric\\Downloads\\P_test\\chromedriver.exe')

browser.get("https://nahlizenidokn.cuzk.cz/VyberParcelu.aspx")

# # elem = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_vyberObecKU_vyberObec_txtObec")
# #
# # elem.send_keys("Turnov")
# obec_vyhledat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_vyberObecKU_vyberObec_btnObec")
# obec_vyhledat.click()
# elem.submit()
#
kat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_vyberObecKU_vyberKU_txtKU")

kat.send_keys("Turnov")
kat_vyhledat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_vyberObecKU_vyberKU_btnKU")
kat_vyhledat.click()

parcela_pred = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_txtParcis")
parcela_pred.send_keys("2773")

parcela_po = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_txtParpod")
parcela_po.send_keys("1")

parcela_vyhledat = browser.find_element_by_css_selector("#ctl00_bodyPlaceHolder_btnVyhledat")
parcela_vyhledat.click()


# print(browser.current_url)
result = requests.get(browser.current_url)

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