#!/usr/bin/env python3
"""Make Use Of Tutorial BS4"""
from bs4 import BeautifulSoup
import requests
import os

website = requests.get("http://192.168.1.129/sister.html")
soup = BeautifulSoup(website.content, "html.parser")

print(website)
input()
print(soup)
input()
print(soup.prettify())
input()
print(soup.text)
input()
os.system("clear")
print(soup.h1)
print(soup.li.prettify())
print(soup.div.text)
input()

a_tags = soup.find_all("a")

[print(tag) for tag in a_tags]
[print(tag.strings) for tag in a_tags]

tags = soup.find_all(["a", "li"])
[print(tag) for tag in tags]

## Does not work
# soup_id = soup.find(id = "tres")
# print(soup_id)
# print(soup_id.text)

## Returns None
# soup_class = soup.find(class_ = "soup")
# print(soup_class)

## Returns None
# div_soup_class = soup.find("div", class_ = "div-soup-class")
# print(div_soup_class)

