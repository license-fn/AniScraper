"""TODO
"""
import argparse
from . import core

def main():
    parser = argparse.ArgumentParser(
        description="Scrape an anime transcript from Anikobin/あにこ便. (http://anicobin.ldblog.jp).")
    parser.add_argument('url', help="The URL of the Anikobin article.")
    parser.add_argument('output_file', help="The output file to write the transcript to.")
    args = parser.parse_args()

    url = args.url
    output_file_name = args.output_file

    bold_tag_strings = core.scrape(url, output_file_name)

    with open(output_file_name, 'w') as f:
        f.write('\n'.join(bold_tag_strings))

main()
