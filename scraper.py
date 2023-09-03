import json,requests,re
from bs4 import BeautifulSoup

def scrape(page, take=None):
    soup     = BeautifulSoup(page.text, 'html.parser')
    listings = soup.find_all('tr', class_='dbaListing')

    if take: listings = listings[:take]

    return [_item(json.loads(listing
        .find('td', class_='mainContent')
        .find('script').text
        .replace('\n', ' ')
        .replace('\r', '')
    )['url']) for listing in listings]

def _item(url):
    page    = requests.get(url)
    soup    = BeautifulSoup(page.text, 'html.parser')
    pattern = re.compile(r"_profile\s+=\s+(\{.*?\})")
    data    = soup.find('script', string=pattern)

    if not data: return None

    json_data = json.loads(data.text.strip()[15:-1])

    return {
        'thing': {
            'id'      : json_data['id'],
            'price'   : json_data['price']['value'],
            'title'   : json_data['title'],
            'text'    : json_data['text'],
            'uploaded': json_data['createdDate']['value'],
            'data'    : json_data['matrixData'],
            'images'  : json_data['images'],
            'url'     : url,
        },
        'user': {
            'id'               : json_data['profile']['ownerId'],
            'name'             : json_data['profile']['name'],
            'address'          : json_data['profile']['address'],
            'validated'        : json_data['profile']['nemIdValidated'],
            'registrationDate' : json_data['profile']['registrationDate']['value'],
            'phone'            : _get_phone(json_data['profile']['contactOptions']),
        },
    }

def _get_phone(contact_options):
    for x in contact_options:
        if x['type'] == 'Phone' and x['dataLink']:
            # TODO Log in - 401 Unauthorized if not logged in session
            r = requests.get(f"https://www.dba.dk{x['dataLink']}")
            return r.json()['data']
    return []
