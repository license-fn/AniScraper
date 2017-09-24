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
beautifulsoup4

Usage:
------
scrape.py <output file> <article url>
"""
import sys

import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
print('URL = {0}'.format(url))

output_file_name = sys.argv[2]
print('OUTPUT = {0}'.format(output_file_name))

page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
bold_tags = soup('b')
bold_tag_strings = map(lambda bt : bt.text, bold_tags)

with open(output_file_name, 'w') as f:
    f.write('\n'.join(bold_tag_strings))
