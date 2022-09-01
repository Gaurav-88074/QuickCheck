from turtle import title
import requests
from bs4 import BeautifulSoup
from code19 import eliminater
with open("doc.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    res = soup.find('div',id="contest-live-upcoming-challenges")
    # cards = soup.find_all('div',class_="contest-card")
    # card = cards[0]

    # title = card.find('div',class_="contest-title")
    # time  = card.find('div',class_="time-container")
    # # time.replace("\n","")
    # print(title.text)
    # print(eliminater(time.text))