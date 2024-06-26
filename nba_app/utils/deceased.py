import requests
from bs4 import BeautifulSoup
import re

def is_deceased(player_name):
    search_url = f"https://en.wikipedia.org/wiki/{player_name.replace(' ', '_')}"
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})
        if infobox:
            for row in infobox.find_all('tr'):
                header = row.find('th')
                if header and 'Died' in header.text:
                    death_info = row.find('td')
                    if death_info:
                        death_text = death_info.text.strip()
                        # Extract death date
                        death_date_match = re.search(r'([A-Za-z]+ \d{1,2}, \d{4})', death_text)
                        death_date = death_date_match.group(1) if death_date_match else "Unknown"

                        # Extract age at death
                        age_at_death_match = re.search(r'\(?aged\s*(\d+)\)?', death_text, re.IGNORECASE) # finally cracked this - how to find age
                        age_at_death = age_at_death_match.group(1) if age_at_death_match else "Unknown"

                        return True, death_date, age_at_death



    return False, None, None
