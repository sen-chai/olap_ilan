# %%
from lxml import html
import requests

with open('./data/Apps em destaque — AppMagic.html', 'r') as fp:
    text = fp.read()
    tree = html.fromstring(text)
# %%
apps = tree.xpath('//a[@title and @target="_blank"]/text()')
apps
len(apps)

# %%
href = tree.xpath('//a[@title and @target="_blank"]/attribute::href')
href
# %%
# acess app detail
detail_url = 'https://appmagic.rocks/google-play/kite-flying-layang-layang/br.pipacombate.maiworm'
requests.get(detail_url).text()

# %%
# select only from first col
