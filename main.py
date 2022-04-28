#!/usr/bin/env python3
"""
main.py file to scrape the weather data in the form of a raw
METAR
"""
import requests
from bs4 import BeautifulSoup as bs

## Airports list
ICAO = ["kstl", "kaln"]

## METAR txt file names list
METAR_FILES = ["kstl.txt", "kaln.txt"]

## Path to write the metar text to
PATH = "/home/pi/metars/"


def request_website(website) -> object:
    """Requests and get the html text from the passed website

    Args:
        website (str): Address to the requested website

    Returns:
        obj: Request object html text
    """
    return requests.get(website)


def get_soup(html_text) -> object:
    """Gets and return the Beautiful Soup text data from the passed
    html text data.

    Args:
        html_text (obj): html text data

    Returns:
        obj: Beautiful Soup html parsed object
    """
    return bs(html_text.content, features="html.parser")


def get_tag(html_text) -> object:
    """Parses and return the text line in the html text with the code
    tag

    Args:
        html_text (obj): Beautiful Soup html object

    Returns:
        obj: Beautiful Soup object of one line with the code html tag
    """
    return html_text.code


def write_metar(metar_text, filename) -> None:
    """Writes the sinle line raw (non-decoded) METAR data to the text file

    Args:
        metar_text (str): Un-decoded METAR text
        filename (str): Filename to write the METAR text to
        PATH (str): Path to the directory to write the text file to
    """
    with open(PATH + filename, "a", encoding="utf-8") as append:
        append.write(metar_text + "\n")


metar_list = []
index = 0
while index < len(ICAO):
    AWC_METAR_SITE = f"https://www.aviationweather.gov/metar/data?ids={ICAO[index]}&format=raw&date=&hours=0"

    awc_page = request_website(AWC_METAR_SITE)
    awc_html = get_soup(awc_page)
    code_tag = get_tag(awc_html)

    ## Sets the metars variable to the metar text between the code tag
    metars = code_tag.children

    for metar in metars:
        write_metar(metar, METAR_FILES[index])

    index += 1
