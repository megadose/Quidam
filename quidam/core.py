#- * -coding: utf - 8 - * -
import requests
import json
from fake_useragent import UserAgent
from evolut import evolut

def instagram(username):
    ua = UserAgent()
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
    if "csrftoken" not in  cookies:
        print("This IP are blocked from instagram. \nPlease change your ip")
        return("")
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
    return(email)

def twitter(username):
    info = evolut(username)
    return(info)

def github(username):
    emails = []
    ua = UserAgent()
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
    if str(r) !="{'message': 'Not Found', 'documentation_url': 'https://developer.github.com/v3/activity/events/#list-events-performed-by-a-user'}":
        for i in r:
            if "commits" in i["payload"].keys():
                for e in i["payload"]["commits"]:
                    if e["author"] not in emails:
                        emails.append(e["author"])
        return(emails)
    else:
        return()
