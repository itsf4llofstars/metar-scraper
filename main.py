#!/usr/bin/env python3
"""
main.py file to scrape the weather data in the form of a raw
METAR
"""
from encodings import utf_8
import os
import requests
from bs4 import BeautifulSoup as bs

os.system("clear")

# Address and ID for scraping
ICAO = "klax"
AWC_METAR_LINK = f"https://www.aviationweather.gov/metar/data?ids={ICAO}&format=raw&date=&hours=0"

# Requests web site data and scrapes html
AWC_PAGE = requests.get(AWC_METAR_LINK)
AWC_HTML = bs(AWC_PAGE.content, features="html.parser")

# Setup constant variables for scraping, pasrsing, and writing text
AWC_STRING = str(AWC_HTML)
AWC_FILE = None
HOURLY_METAR = None
METAR_FILE_NAME = "metars.txt"


# Writes scraped html to text file
try:
    with open(f"/home/pi/python/metar-scraper/{ICAO}-metar.txt", 'w') as w:
        AWC_FILE = w.write(AWC_STRING)
except FileNotFoundError as fnfe:
    print(f"{fnfe}")

# Reads in html scraped text and parses out the metar text line
try:
    with open(f"/home/pi/python/metar-scraper/{ICAO}-metar.txt", 'r') as r:
        html_text = r.readlines()
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
else:
    for line in html_text:
        if (ICAO.upper() in line) and line.startswith("<code>"):
            HOURLY_METAR = line[6:-13]
            break

# Deletes unused text file
os.unlink(f"/home/pi/python/metar-scraper/{ICAO}-metar.txt")

# Appends the raw METAR text to text file
try:
    with open(f"/home/pi/python/metar-scraper/{METAR_FILE_NAME}", "a") as append:
        append.write(HOURLY_METAR)
        append.write("\n")
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
