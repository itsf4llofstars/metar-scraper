#!/usr/bin/env python3
"""cron-metar.py Script to check, scrape and write METAR data on an
hourly basis. Used as a cron script.
"""
import requests
import time
from bs4 import BeautifulSoup as bs



def main():
    """main function"""
    # icao id's for airports
    KALN = "KALN"
    KSTL = "KSTL"

    # Web address to scrape
    AWC_METAR_KALN = f"https://www.aviationweather.gov/metar/data?ids={KALN}&format=raw&date=&hours=0"
    AWC_METAR_KSTL = f"https://www.aviationweather.gov/metar/data?ids={KSTL}&format=raw&date=&hours=0"

    # request web-site data
    KALN_PAGE = requests.get(AWC_METAR_KALN)
    time.sleep(1.0)
    KSTL_PAGE = requests.get(AWC_METAR_KSTL)

    # Scrape html's
    KALN_HTML = bs(KALN_PAGE.content, features="html.parser")
    KSTL_HTML = bs(KSTL_PAGE.content, features="html.parser")

    # set constant variables for parsing and writing
    KALN_STR = str(KALN_HTML)
    KALN_FILE = None
    KALN_HR_METAR = None
    KALN_FILE = "kaln-metar.txt"

    KSTL_STR = str(KSTL_HTML)
    KSTL_FILE = None
    KSTL_HR_METAR = None
    KSTL_FILE = "kaln-metar.txt"


if __name__ == "__main__":
    main()
