""" Contains the core logic of the scraper.
"""
import logging
import requests
from bs4 import BeautifulSoup

LOGGER = logging.getLogger(__name__)

def scrape(ani_url, output_file, timeout=10):
    ''' Scrapes an anime transcript from Anikobin to the specified file.

    Parameters:
    -----------
    ani_url : string
      The URL of the Anikobin article.
    output_file : string
      The path of the output file.
    timeout : double
      [Optional] The number of seconds to wait until the HTTP request times out.
      Defaults to 10s.
    '''
    LOGGER.debug('Scraping "%s" -> "%s"', ani_url, output_file)

    # Perform a GET request for the `ani_url`
    LOGGER.debug('Performing GET request...')
    response = requests.get(ani_url, timeout=timeout) # requests.exceptions.timeout

    # Raise an exception if the server failed
    LOGGER.debug('Response code = %d (%s)', response.status_code, response.reason)
    response.raise_for_status() # requests.exceptions.httperror

    # Pull transcript.
    # Character quotes are indicated by HTML bold tags.
    soup = BeautifulSoup(response.content, "html.parser")
    bold_tags = soup('b')
    return map(lambda bt: bt.text, bold_tags)
