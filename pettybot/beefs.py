import urllib.request as url
from bs4 import BeautifulSoup
from random import randint, sample
import re 


def halo_beef():
    pages = ['']

    for ind in range(1,20):
        pages.append('/.p' + str(ind)) 

    names = []
    nums = []

    for page in pages:
        address = 'https://steamcharts.com/top' + page
        req = url.Request(address, headers={'User-Agent' : "surf"}) 
        page = url.urlopen(req)
        soup = BeautifulSoup(page, 'html.parser')

        games = soup.find_all('tr')[1:]

        for game in games:
            name = game.find('td', attrs={'class':'game-name left'})
            name = name.text.strip()
            names.append(name)

            num = game.find('td', attrs={'class':'num'})
            num = num.text.strip()
            nums.append(int(num))
    
    halo_index = names.index('Halo: The Master Chief Collection')
    halo_num = nums[halo_index]
    
    if halo_index <= 49:
        return 'Fair Enough...Halo is in the top 50 at least'

    other_index = randint(50, halo_index-1)
    other_name = names[other_index]
    other_num = nums[other_index]

    return 'Halo: The Master Chief Collection is so shit that it only has ' + str(halo_num) \
            + ' players. Even less than ' + other_name + ' with ' + str(other_num) \
            + ' players. HAHAHAHAHAHAHAHAHA!!!!!11!!'

def twitch_beef():
    pages = ['','?page=2','?page=3','?page=4','?page=5']
    page = sample(pages,1)[0] 
    
    address = 'https://www.twitchquotes.com/copypastas' + page
    req = url.Request(address, headers={'User-Agent' : "surf"}) 
    page = url.urlopen(req)
    soup = BeautifulSoup(page, 'html.parser')
    
    quotes = soup.find_all('div', attrs={'class':'quote_text_multi_line'})
    quote = None

    while quote is None:
        index = randint(0, len(quotes)-1)
        quote = quotes[index].find('span', attrs={'id' : re.compile(r'^quote_display_content_')})
    print(index, quote.text.strip())
    return quote.text.strip()



