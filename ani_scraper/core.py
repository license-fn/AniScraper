"""Scrape an anime transcript from Anikobin/あにこ便. (http://anicobin.ldblog.jp).

Anikobin publishes articles on anime episodes. Each article consists
of a large portion of the show's transcript. This transcript is
expecially helpful for practicing reading and listening comprehension
while watching anime.

This script pulls the transcript from an article and writes it to a
text file. Accuracy is no 100% correct at the moment, but it is close
enough to get the job done.

Requirements:
------------
Python 3
beautifulsoup4>=4.6
requests>=2.18

Usage:
------
python3 ani-scrape.py <output file> <article url>
"""
import logging
import requests
from bs4 import BeautifulSoup

LOGGER = logging.getLogger(__name__)

def scrape(ani_url, output_file, timeout=None):
    LOGGER.debug('Scraping "%s" -> "%s"', ani_url, output_file)

    # Set timeout, if specified
    kwargs = {}
    if timeout is not None:
        LOGGER.debug('Set timeout = %d', timeout)
        kwargs['timeout'] = timeout

    # Perform a GET request for the `ani_url`
    LOGGER.debug('Performing GET request...')
    response = requests.get(ani_url, timeout) # requests.exceptions.timeout

    # Raise an exception if the server failed
    LOGGER.debug('Response code = %d (%s)', response.status_code, response.reason)
    response.raise_for_status() # requests.exceptions.httperror

    soup = BeautifulSoup(response.content, "html.parser")
    bold_tags = soup('b')
    return map(lambda bt: bt.text, bold_tags)
