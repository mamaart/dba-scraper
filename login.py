import re, json
from bs4 import BeautifulSoup

def send_msg(session, url, msg=''):
    def get_uid(soup):
        pattern = re.compile(r"_profile\s+=\s+(\{.*?\})")
        data    = soup.find('script', text=pattern).text.strip()
        data    = data[15:-1]
        return json.loads(data)['id']

    soup = BeautifulSoup(session.get(url).text, 'html.parser')
    uid = get_uid(soup)['id']
    return session.post(
        url = f'https://www.dba.dk/api/dba-vip-site/{uid}/conversation/buyer/chat',
        json={
            "__type":"Dba.Dba.ExternalApiV2.Services.Listing.Messages.Conversation.BuyerChatCreatedRequest, Dba.Dba.ExternalApiV2",
            "externalId": uid,
            "text": msg,
            "cannedType":None,
        },
    ).ok
