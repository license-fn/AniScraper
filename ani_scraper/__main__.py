"""Serves as an entry point for the ani_scraper package.

This is also invoked from the executable script provided within
setup.py.

Contains logic for running the package as an application.
"""
import argparse
import requests
from . import core

def main():
    """ The entry point of the package when run as a command line application.
    """
    parser = argparse.ArgumentParser(
        description=('Scrape an anime transcript from Anikobin/あにこ便. (http://anicobin.ldblog.jp).'))
    parser.add_argument('url', help='The URL of the Anikobin article.')
    parser.add_argument('output_file', help='The output file to write the transcript to.')

    # Pull out args
    args = parser.parse_args()
    url = args.url
    output_file_name = args.output_file

    # Grab transcript and write to file.
    try:
        transcript = core.scrape(url, output_file_name)
        with open(output_file_name, 'w') as f:
            f.write('\n'.join(transcript))
    except requests.exceptions.Timeout:
        print('The connection timed out.')
    except requests.exceptions.HTTPError as err:
        print('The page returned an HTTP error. (Code: {0})'.format(err.response.status_code))

main()
