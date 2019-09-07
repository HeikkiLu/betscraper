
import os, datetime, os
from scrape import scrape
'''

* Started 22.5.2019
* Complete 26.7.2019
* Modified project structure on 7.9.2019
* Heikki Luukkonen

Program scrapes cbs sport bet tips for mlb and saves them to excel

'''

def main():
        # Checking the date for url and excel
        x = datetime.datetime.now()
        date_url = x.strftime("%Y%m%d")
        date = x.strftime("%A %d. %B %Y")

        # Call for function to scrape the games
        scrape(date_url, date)

if __name__ == "__main__":
        #os.chdir('H:\\Python\\Projektit\\Webscrape\\mlb\\Data')
        main()