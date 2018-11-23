# from pudb import set_trace; set_trace()
import requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urlparse
# import re

# get the data
data = requests.get('https://www.365chess.com/chess-games.php').content



# load data into bs4
# soup = BeautifulSoup(data.text, 'html.parser')
player = 0
soup = BeautifulSoup(data, features='html.parser', parse_only=SoupStrainer('a', href=True))
for link in soup.find_all("a", href=True):
    de_url=link.get("href")
    print(de_url)
    if "/players/" in de_url:
        if player > 2:
            print("ATTENTIE, de waar de van de index player is te hoog: ", player)
            player = 0
        elif player == 2:
            print("de waarde van player is: ", player)
            player += 1
            url_speler_zwart = urlparse(de_url)
            print("url_speler_zwart: ", url_speler_zwart)
            speler_zwart = url_speler_zwart.rsplitlink('/',1)[-1]
            print(speler_zwart)

        else:
            print("de waarde van player is: ", player)
            player += 1
            url_speler_wit = urlparse(link.get("href"))
            print("url_speler_wit: ", url_speler_wit)
            speler_wit = url_speler_wit.rsplitlink('/',1)[-1]
            print(speler_wit)
        
    if "javascript:Popup" in link.get("href"):
        javascript_popup_url = link['href'][18:-1]
        print(javascript_popup_url)

# pattern = re.compile(r"javascript:Popup\('(.*?)'\);")

# href = soup.find('a', href=pattern)["href"]
# link = pattern.search(href).group(1)
# print(link)  # prints ../UploadFile/Images/c/1/B_27902.jpg
