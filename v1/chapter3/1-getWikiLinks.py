from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


"""p.53, final code"""
random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

# """p.51, 1st iteration"""
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.find_all("a"):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# """p.52, 2nd iteration"""
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("(/wiki/)((?!:).)*$")):
#     if "href" in link.attrs:
#         print(link.attrs["href"])
