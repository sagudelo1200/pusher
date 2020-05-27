#!/usr/bin/env python2
"""Main entry point for tasker

Usage:
    `./tasker.py https://intranet.hbtn.io/projects/231`
"""
from scrapers import *


def get_args():
    """Method that grabs argv

    Returns:
        link (str): argv[1]
    """
    arg = sys.argv[1:]
    count = len(arg)

    if count > 1:
        print("[ERROR] Too many arguments (must be one)")
        sys.exit()
    elif count == 0:
        print("[ERROR] Too few arguments (must be one)")
        sys.exit()

    link = sys.argv[1]
    return link


def tasker():
    """Entry point for tasker

    Scrapes for specific text to create a .tasks automatically.
    """

    url = get_args()

    print("\nPusher version 1.1")
    print("Creating .tasks file:")
    parse_data = BaseParse(url)

    sys.stdout.write("  -> Scraping information... ")
    # Creating scraping object
    r_scraper = ReadScraper(parse_data.soup)

    print("done")

    # Writing to .tasks with scraped data
    r_scraper.open_tasks()
    r_scraper.write_symple_tasks()
    os.system("echo '.tasks' >> .gitignore")

    print(".tasks all set!")


if __name__ == "__main__":
    tasker()
