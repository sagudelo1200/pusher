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
        print('\033[91m[X] Pusher:\033[0m Too many arguments(must be one)')
        sys.exit()
    elif count == 0:
        print('\033[34m[?] Usage:\033[0m tasker <intranet_project_url>')
        sys.exit()

    link = sys.argv[1]
    return link


def tasker():
    """Entry point for tasker

    Scrapes for specific text to create a .tasks automatically.
    """

    url = get_args()

    print(
        "\n\033[34m<<<\033[0m \033[4mPusher version 1.1\033[0m\033[34m >>>\033[0m\n")
    print("Getting intranet data for tasks...\n")
    parse_data = BaseParse(url)

    sys.stdout.write("  -> Scraping information... ")
    # Creating scraping object
    r_scraper = ReadScraper(parse_data.soup)

    print("done")

    # Writing to .tasks with scraped data
    r_scraper.open_tasks()
    r_scraper.write_symple_tasks()
    os.system("echo '.tasks' >> .gitignore")

    print(
        "\n\033[92mSuccessfully completed tasks and stored in the .task file!\n")


if __name__ == "__main__":
    tasker()
