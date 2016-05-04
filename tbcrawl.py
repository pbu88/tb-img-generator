import bs4
import requests
import re
import StringIO

def fetch_page(url):
    r = requests.get(url)
    return r.content

def get_background(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    bkgrounds_div = soup.find('div', {'class':'offer__hero'}).find('div').findAll('span')
    data_srcs = map(
        lambda s: s['data-src'],
        filter(lambda s: re.search(r'\/offer-cover-image\/', s['data-src']),
               bkgrounds_div))
    if not data_srcs:
        return None
    bk_url = data_srcs[0]
    bk_img = requests.get('http:' + bk_url)
    bk_buff = StringIO.StringIO(bk_img.content)
    return bk_buff
