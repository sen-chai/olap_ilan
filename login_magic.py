# %%
import time
from selenium import webdriver
from lxml import html
import requests
url = 'https://appmagic.rocks/top-charts/apps?country=BR&topDepth=1000&date=2015-01-01&aggregation=year&store=1'

page = requests.get(url)
with open('./data/magic_apps.html', 'w') as fp:
    fp.write(page.text)
tree = html.fromstring(page.content)
# %%
DRIVER_PATH = './chromedriver'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver = webdriver.Firefox()
url = 'https://appmagic.rocks/top-charts/apps?country=BR&topDepth=1000&date=2015-01-01&aggregation=year&store=1'
driver.get(url)
time.sleep(10)
# %%
executor_url = driver.command_executor._url
session_id = driver.session_id

with open('session.txt', 'w') as f:
    f.write(f'{session_id}\n{executor_url}')
