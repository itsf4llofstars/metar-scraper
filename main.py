#!/usr/bin/env python3
"""main.py file to scrape the weather dat in the form of a raw
METAR"""
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
print(awc_html)
