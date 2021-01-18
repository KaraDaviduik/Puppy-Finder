import requests
from bs4 import BeautifulSoup
import time
import messages


sleep_time = 120 # checks kijiji again after this amount of seconds

# I am working on converting all of the methods within kijiji() into individual methods
def kijiji():
    abort = False
    puppy_dict = {}
    count = 0
    
    try:
        while(not abort):
        
            # scrapes kijiji to get all of the puppies
            # For reference the URL that I used is: https://www.kijiji.ca/b-chiens-chiots/quebec/c126l9001?ad=offering
            URL = ''
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            puppies = soup.find_all('div', class_="search-item regular-ad")
            
            # parses the HTML to get puppy attributes
            for puppy in puppies:
                ad_title = puppy.find('a', class_='title').text.strip()
                cost = puppy.find('div', class_='price').text.strip()
                distance = puppy.find('div', class_='distance').text.strip()
                description = puppy.find('div', class_='description').text.strip()
                link = 'https://www.kijiji.ca' + puppy.find('a')['href']
                ID = puppy.attrs['data-listing-id']
                
                
                if ID not in puppy_dict:
                    puppy_dict[ID] = (ad_title, cost, distance)
                    # known issue: only page 1 is scraped, so if an ad on page 1 is deleted, there will be 
                    # a "new" ad alert which is just a puppy ad previously on page 2 now appearing on page 1
                    # working on fixing this
                    if count > 0:
                        print("**************************")
                        print("!!!!!NEW PUPPY ALERT!!!!!!")
                        print("**************************")
                        # sends new puppy alert
                        messages.send_message_kijiji(ad_title, link, description, cost)
                        
            count = 1
            # checks kijiji again after sleep_time
            time.sleep(sleep_time)
    
    # restarts the scraper if there's an error
    except Exception as e:
        print(e)
        kijiji()

try:
    kijiji()
except:
    messages.twilio_send_sms("Kijiji scraper stopped working")