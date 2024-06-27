import requests
from bs4 import BeautifulSoup
import re
from django.core.cache import cache

def is_deceased(player_name):
    cache_key = f"deceased_{player_name.lower().replace(' ', '_')}"
    cached_result = cache.get(cache_key)
    if cached_result:
        return cached_result

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
                        death_date_match = re.search(r'([A-Za-z]+\s+\d{1,2},\s+\d{4}|[0-9]+\s+[A-Za-z]+\s+\d{4})', death_text)
                        death_date = death_date_match.group(1) if death_date_match else "Unknown"

                        # Extract age at death
                        age_at_death_match = re.search(r'\(aged\s*(\d+)\)', death_text, re.IGNORECASE)
                        age_at_death = age_at_death_match.group(1) if age_at_death_match else "Unknown"

                        result = (True, death_date, age_at_death)
                        cache.set(cache_key, result, timeout=60*60*24) 
                        return result

    result = (False, None, None)
    cache.set(cache_key, result, timeout=60*60*24)  # 24 hours
    return result
