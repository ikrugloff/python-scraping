from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

"""p.58 - final"""
pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())  # Получаем заголовок
        print(bsObj.find(id ="mw-content-text").findAll("p")[0])  # Получаем текстовый контент
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])  # Получаем кнопку "Edit"
        # Кнопка "Edit" размещается только на тех страницах, которые уже содержат как заголовки, так и текстовый
        # контент, но она есть не на всех этих страницах.
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")

#
# """p.56 - 1st edition"""
# pages = set()
#
#
# def getLinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
#         if "href" in link.attrs:
#             if link.attrs["href"] not in pages:
#                 newPage = link.attrs["href"]
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
#
# getLinks("")
