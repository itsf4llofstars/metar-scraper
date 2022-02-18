#!/usr/bin/env python3
"""
main.py file to scrape the weather data in the form of a raw
METAR
"""
import os
import re
import requests
import sys
from bs4 import BeautifulSoup as bs

os.system("clear")

icao = 'kaln'
AWC_METAR = f"https://www.aviationweather.gov/metar/data?ids={icao}&format=raw&date=&hours=0"

awc_page = requests.get(AWC_METAR)
awc_html = bs(awc_page.content, features="html.parser")
awc_string = str(awc_html)
awc_file = None

try:
    with open(f"/home/pi/python/metar-scraper/{icao}-metar.txt", 'w') as w:
        awc_file = w.write(awc_string)
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
except Exception as err:
    print(f"{err}")

hourly_metar = None
try:
    with open(f"/home/pi/python/metar-scraper/{icao}-metar.txt", 'r') as r:
        html_text = r.readlines()
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
except Exception as err:
    print(f"{err}")
else:
    for line in html_text:
        if (icao.upper() in line) and line.startswith("<code>"):
            hourly_metar = line[6:-13]
            break

print(hourly_metar)
