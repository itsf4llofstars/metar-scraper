#!/usr/bin/env python3
"""cron-metar.py Script to check, scrape and write METAR data on an
hourly basis. Used as a cron script.
Released as ver. 1.1
"""
import re
import time
import requests
from bs4 import BeautifulSoup as bs

# TODO: Create functions for all that can be functions from main


def write_metar(file_name, metar) -> None:
    """Writes the METAR to a file"""
    try:
        with open(f"/home/bumper/Documents/{file_name}", "a") as append:
            append.write(metar)
            append.write("\n")
    except OSError as os_err:
        print(f"{os_err}")


def main():
    """main function"""
    # icao id's for airports
    kaln = "kaln"
    kstl = "kstl"

    # web address to scrape
    awc_metar_kaln = (
        f"https://www.aviationweather.gov/metar/data?ids={kaln}&format=raw&date=&hours=0"
    )
    awc_metar_kstl = (
        f"https://www.aviationweather.gov/metar/data?ids={kstl}&format=raw&date=&hours=0"
    )

    # request web-site data
    kaln_page = requests.get(awc_metar_kaln)
    time.sleep(1.0)
    kstl_page = requests.get(awc_metar_kstl)

    # Scrape html's
    kaln_html = bs(kaln_page.content, features="html.parser")
    kstl_html = bs(kstl_page.content, features="html.parser")

    # set constant variables for parsing and writing
    kaln_file = "kaln-metar.txt"
    kstl_file = "kstl-metar.txt"

    # find the stations icao in the code tag
    kaln_metar = kaln_html.find_all("code", string=re.compile(r"KALN"))[0]
    kstl_metar = kstl_html.find_all("code", string=re.compile(r"KSTL"))[0]

    # create string from the regex returned tag line
    kaln_metar_str = str(kaln_metar)[6:-7]
    kstl_metar_str = str(kstl_metar)[6:-7]

    # append METAR wx to file
    write_metar(kaln_file, kaln_metar_str)
    write_metar(kstl_file, kstl_metar_str)


if __name__ == "__main__":
    main()
