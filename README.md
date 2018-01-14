# AniScraper

Scrape an anime transcript from Anikobin/あにこ便. (http://anicobin.ldblog.jp)

Anikobin publishes articles on anime episodes. Each article consists
of a large portion of the show's transcript. This transcript is
expecially helpful for practicing reading and listening comprehension
while watching.

This Python script pulls the anime transcript from an article and writes it to a
text file. Accuracy is not 100% correct at the moment, but it is close
enough to get the job done.

## Usage:
Once installed, `ani_scraper` is available both as a command line executable and as a module.
* As an executable, it can be invoked via: `ani_scraper`
* As a module, it can be invoked via: `python3 -m ani_scraper`

```
ani_scraper [-h] url output_file

Scrape an anime transcript from Anikobin/あにこ便. (http://anicobin.ldblog.jp)

positional arguments:
  url          The URL of the Anikobin article.
  output_file  The output file to write the transcript to.

optional arguments:
  -h, --help   show this help message and exit
```

## Installation

### Requirements:
* Python3
* pip
* make

### From source
1. Clone the repository
2. Run `make`
3. Run `make install`
    * This command uses `pip` to install the wheel built in step (2). If you are using a python virtual environment, be sure to activate it before installing.
