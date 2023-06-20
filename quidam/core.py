#- * -coding: utf - 8 - * -
import requests
import json
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)
import cfscrape,urllib3
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context, DEFAULT_CIPHERS
from fake_headers import Headers
# urllib3.util.ssl_.DEFAULT_CIPHERS = DEFAULT_CIPHERS
DEFAULT_CIPHERS += ':!SHA1'

def evolut(account):
    class CustomAdapter(HTTPAdapter):
        def init_poolmanager(self, *args, **kwargs):
            ctx = create_urllib3_context(ciphers=DEFAULT_CIPHERS)
            super(CustomAdapter, self).init_poolmanager(*args, ssl_context=ctx, **kwargs)

    header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
    )
    scraper = cfscrape.create_scraper()
    scraper.mount('https://', CustomAdapter())
    url = "https://twitter.com/account/begin_password_reset"
    #print(url)
    req = scraper.get(url,headers=header.generate())
    soup = BeautifulSoup(req.text, 'html.parser')
    authenticity_token = soup.input.get('value')
    data = {
      'authenticity_token': authenticity_token,
      'account_identifier': account
    }
    cookies = req.cookies
    response = scraper.post(url, cookies=cookies, data=data,headers=header.generate())
    soup2 = BeautifulSoup(response.text, 'html.parser')
    try:
        if(soup2.find('div', attrs = {'class' : 'is-errored'}).text=="Please try again later."):
            return("Rate limit change your ip")
    except:
        pass
    try:
        info = soup2.find('ul', attrs = {'class' : 'Form-radioList'}).findAll("strong")
    except:
        return("Not email or phone")
    try:
        phone = int(info[1].text)
        email = str(info[0].text)
    except:
        email = str(info[0].text)
    if(len(info)==2):
        return({"phone":phone,"email":email})
    else:
        return({"email":email})
 

def instagram(username):
    s = requests.Session()
    s.headers = {
    'User-Agent': ua.random,
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
    }
    r = s.get('https://www.instagram.com/accounts/password/reset/?hl=fr')
    #print(r.content)
    cookies = s.cookies.get_dict()

    if "csrftoken" not in cookies:
        crsf = str(r.content).split('{"csrf_token":"')[1].split('"')[0]
    else:
        crsf = cookies["csrftoken"]

    headers = {
        'User-Agent': ua.random,
        'Accept': '*/*',
        'X-CSRFToken': crsf,
        'X-IG-WWW-Claim': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.instagram.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/accounts/password/reset/?hl=fr',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
    }

    params = (
        ('hl', 'fr'),
    )

    data = {
      'email_or_username': username,
      'recaptcha_challenge_field': ''
    }

    response = requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/', headers=headers, params=params, cookies=cookies, data=data)
    emailScrape = response.text.split("pour")[0].split(" ")
    email = emailScrape[len(emailScrape)-2]
    if len(email) > 5:
        return(email)
    else:
        return("NULL")
def twitter(username):
    info = evolut(username)
    return(info)

def github(username):
    emails = []
    s = requests.Session()
    s.headers = {
    'User-Agent': ua.random,
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
    }
    r = s.get("https://api.github.com/users/"+username+"/events")
    r = json.loads(r.text)
    if r.get('message', '') == 'Not Found':
        return()
    for i in r:
        if "commits" in i["payload"].keys():
            for e in i["payload"]["commits"]:
                if e["author"] not in emails:
                    emails.append(e["author"])
            return(emails)
