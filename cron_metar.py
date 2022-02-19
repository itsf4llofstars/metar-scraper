#!/usr/bin/env python3
"""cron-metar.py Script to check, scrape and write METAR data on an
hourly basis. Used as a cron script.
"""
import requests
import time
import re
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
    KALN_FILE = "kaln-metar.txt"
    KSTL_FILE = "kaln-metar.txt"

    kaln_metar = KALN_HTML.find_all("code", string=re.compile(r"KALN"))[0]
    kstl_metar = KSTL_HTML.find_all("code", string=re.compile(r"KSTL"))[0]

    kaln_metar_str = str(kaln_metar)[6:-7]
    kstl_metar_str = str(kstl_metar)[6:-7]

    print(kaln_metar_str)
    print(kstl_metar_str)


if __name__ == "__main__":
    main()
