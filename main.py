#!/usr/bin/env python3
"""main.py file to scrape the weather dat in the form of a raw
METAR"""
import os
import re
import sys
from bs4 import BeautifulSoup as bs

os.system("clear")
