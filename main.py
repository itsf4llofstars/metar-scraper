#!/usr/bin/env python3
"""
main.py file to scrape the weather data in the form of a raw
METAR
"""
import os
import requests
from bs4 import BeautifulSoup as bs

os.system("clear")

ICAO = "kord"
AWC_METAR = f"https://www.aviationweather.gov/metar/data?ids={ICAO}&format=raw&date=&hours=0"

AWC_PAGE = requests.get(AWC_METAR)
AWC_HTML = bs(AWC_PAGE.content, features="html.parser")
AWC_STRING = str(AWC_HTML)
AWC_FILE = None

try:
    with open(f"/home/pi/python/metar-scraper/{ICAO}-metar.txt", 'w') as w:
        AWC_FILE = w.write(AWC_STRING)
except FileNotFoundError as fnfe:
    print(f"{fnfe}")

HOURLY_METAR = None
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

os.unlink(f"{ICAO}-metar.txt")

METAR_FILE_NAME = "metars.txt"
try:
    with open(f"/home/pi/python/metar-scraper/{METAR_FILE_NAME}", "a") as append:
        append.write(HOURLY_METAR)
        append.write("\n")
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
