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

## Path to write the metar text to
PATH = "/home/pi/metars/"


def request_website(website):
    return requests.get(website)


def get_soup(html_text):
    return bs(html_text.content, features="html.parser")


def get_tag(html_text):
    return html_text.code


def write_metar(metar_text, filename):
    global PATH
    with open(PATH + filename, "a") as append:
        append.write(metar_text + "\n")


metar_list = []
index = 0
while index < len(ICAO):
    ## Web address to be scraped
    AWC_METAR_SITE = f"https://www.aviationweather.gov/metar/data?ids={ICAO[index]}&format=raw&date=&hours=0"

    awc_page = request_website(AWC_METAR_SITE)
    awc_html = get_soup(awc_page)

    ## Sets code_tag variable to the html line with the metar
    code_tag = get_tag(awc_html)

    ## Sets the metars variable to the raw metar text
    metars = code_tag.children

    [write_metar(metar, METAR_FILES[index]) for metar in metars]

    index += 1
