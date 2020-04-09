import requests
from bs4 import BeautifulSoup

result = requests.get("https://nahlizenidokn.cuzk.cz/ZobrazObjekt.aspx?encrypted=n0sDDl2onCj8BvefxwvMM0gLG29BUUGHqXZGRWtuqPDw8gDs6Zb8HJQ8y6fGLys0o4aO5JvxBMrC8t-6Tl7lVWfV_mvTwwOChF87fBJBUdQDELPvhqAFUAsVNglR6K78")

print(result.status_code)

src = result.content
soup = BeautifulSoup(src, "html.parser")
links = soup.find_all("td")

# print(links)
text = soup.get_text()
text1 = " ".join(text.split())
print(text1)
