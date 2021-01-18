import requests
from bs4 import BeautifulSoup
import time
import messages



sleep_time = 120 # checks SPCA again after this amount of time

def SPCA():
    abort = False
    puppy_dict = {}
    count = 0
    
    try:
        while(not abort):
            
            # scrapes SPCA to get all of the puppies
            # URL I used was https://www.spca.com/en/adoption/dogs-for-adoption/
            URL = ''
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(class_="row pet--row")
            puppies = results.find_all('div', class_='pet--card')
            
            # parses the HTML to get puppy attributes
            for puppy in puppies:
                puppy_name = puppy.find('h5', class_='card--title').text.strip()
                puppy_info = puppy.find('div', class_='pet--infos').text.strip()
                link = puppy.find('a')['href']
                
                if puppy_name not in puppy_dict:
                    puppy_dict[puppy_name] = puppy_info
                    if count > 0:
                        print("**************************")
                        print("!!!!!NEW PUPPY ALERT!!!!!!")
                        print("**************************")
                        # sends new puppy alert
                        messages.send_message_SPCA(puppy_name, link, puppy_info)
            
            count = 1
            # checks SPCA again after sleep_time
            time.sleep(sleep_time)
            
    # restarts the scraper if there's an error
    except Exception as e:
        print(e)
        SPCA()
        
try:
    SPCA()
except:
    messages.twilio_send_sms("SPCA scraper stopped working")
