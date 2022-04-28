#!/usr/bin/env python3
"""
main.py file to scrape the weather data in the form of a raw
METAR
"""
from encodings import utf_8
import requests
from bs4 import BeautifulSoup as bs

## Airports list
ICAO = ["kstl", "kaln"]

## METAR txt file names list
METAR_FILES = ["kstl.txt", "kaln.txt"]

## Path to text metar text files
PATH = "/home/pi/metars/"


def request_website(website):
    return requests.get(website)


index = 0
while index < len(ICAO):
    ## Web address to be scraped
    AWC_METAR_SITE = f"https://www.aviationweather.gov/metar/data?ids={ICAO[index]}&format=raw&date=&hours=0"

    ## Requests web site data
    #awc_page = requests.get(AWC_METAR_LINK)
    awc_page = request_website(AWC_METAR_SITE)

    ## Beautiful Soup scraping of the web-site data
    awc_html = bs(awc_page.content, features="html.parser")

    ## Sets variable to the line that has the METAR text data
    code_tag = awc_html.code

    ## Print debug
    for metar in code_tag.children:
        print(metar)

    index += 1

'''
AWC_STRING = str(AWC_HTML)
AWC_FILE = None
HOURLY_METAR = None
METAR_FILE_NAME = "metars.txt"


# Writes scraped html to text file
try:
    with open(f"/home/$USER/python/metar-scraper/{ICAO[index]}-metar.txt", 'w') as w:
        AWC_FILE = w.write(AWC_STRING)
except FileNotFoundError as fnfe:
    print(f"{fnfe}")

# Reads in html scraped text and parses out the metar text line
try:
    with open(f"/home/$USER/python/metar-scraper/{ICAO[index]}-metar.txt", 'r') as r:
        html_text = r.readlines()
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
else:
    for line in html_text:
        if (ICAO[index].upper() in line) and line.startswith("<code>"):
            HOURLY_METAR = line[6:-13]
            break

# Deletes unused text file
os.unlink(f"/home/$USER/python/metar-scraper/{ICAO[index]}-metar.txt")

# Appends the raw METAR text to text file
try:
    with open(f"/home/$USER/python/metar-scraper/{METAR_FILE_NAME}", "a") as append:
        append.write(HOURLY_METAR)
        append.write("\n")
except FileNotFoundError as fnfe:
    print(f"{fnfe}")
'''
