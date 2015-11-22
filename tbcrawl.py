import bs4
import requests
import re
import StringIO

def fetch_page(url):
    r = requests.get(url)
    return r.content

def get_logo(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    logo = soup.find('img', {'class':'Logo-img'})
    if logo is None:
        return None
    logo_onerror = logo.get('onerror')
    match = re.search(r'(//.*\.png)', logo_onerror)
    if match is None:
        return None
    logo_url = match.group(0)
    logo_img = requests.get('http:' + logo_url)
    logo_buff = StringIO.StringIO(logo_img.content)
    return logo_buff

def get_background(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    bkground = soup.find('header', {'class':'offer-header'})
    if bkground is None:
        return None
    bkground_style = bkground.get('style')
    match = re.search(r"url\('(.*)'\)", bkground_style)
    if match is None:
        return None
    bk_url = match.group(1)
    bk_img = requests.get('http:' + bk_url)
    bk_buff = StringIO.StringIO(bk_img.content)
    return bk_buff
