import requests
from filewrite import filewrite
from itertools import chain 
from bs4 import BeautifulSoup as bs

def scrape(date_url, datefw):

        # Getting todays site
        response = requests.get('https://www.cbssports.com/mlb/expert-picks/'+date_url)
        # Souping data
        soup = bs(response.text, 'lxml')

        # Finds all span id's with class as a team
        teams = soup.findAll('span', class_='team')
        
        # Finding all over/under bets
        our = soup.findAll(class_="expert-ou")

        # Finds text and adds to list
        lines = [our.get_text() for our in our]
        ou_bets = list(map(str.strip, lines))
        
        k = " "
        N = 1

        res = list(chain(*[ou_bets[i : i+N] + [k]  
            if len(ou_bets[i : i+N]) == N  
            else ou_bets[i : i+N]  
            for i in range(0, len(ou_bets), N)])) 


        # Data from todayspairs
        rtodayspairs = []

        # Loops page and gets teams under a anchor, sends them to rtodayspairs which will be a tuple
        for a_tag in teams:
                # Game pairs
                pairs = (a_tag.text, a_tag.next_sibling)
                rtodayspairs.append(pairs)

        # Tuple to list
        convert_rtodayspairs = list(map(list, rtodayspairs)) 

        # Nested list to normal
        todayspairslist = [item for sublist in convert_rtodayspairs for item in sublist]

        # Cleaning the list
        todayspairs1 = list(map(str.strip, todayspairslist))

        # More cleaning...
        todayspairs2 = [pair for pair in todayspairs1 if pair.strip()]
        
        # Pairing teams, no need for this..
        # todayspairs = [todayspairs2[i:i+2] for i in range(0, len(todayspairs2), 2)]

        if not todayspairs2:
                print('No games found for today...')
        
        else:
                # Calling function to save data to excel
                filewrite(datefw, todayspairs2, res)

       