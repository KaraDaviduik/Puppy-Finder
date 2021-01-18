# Puppy-Finder

The Puppy Finder is a Python web scraper for the kijiji and SPCA websites that notifies you via SMS when new dogs are added. My work was extended by George Tzavelas https://github.com/georgetzavelas/puppy_finder!

To set up the scraper, open kijiji.py and/or SPCA.py and add the specific URL(s) you wish to scrape. 

messages.py requires a Twilio account_sid, auth_token, and from_phone_number which can be set up for free [here](https://www.twilio.com/try-twilio). Also add to_phone_number, which is the phone number that will be sent SMS alerts.

After this information has been added, simply run the kijiji.py and/or SPCA.py programs :)
