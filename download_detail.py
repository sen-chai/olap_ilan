# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()

urls = ['https://appmagic.rocks/google-play/kite-flying-layang-layang/br.pipacombate.maiworm',
        'https://appmagic.rocks/google-play/kite-flying-layang-layang/br.pipacombate.maiworm', 'https://appmagic.rocks/google-play/whatsapp-messenger/com.whatsapp']

app_tags = []
for url in urls:
    driver.get(url)
    try:
        elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, 'application-tags'))  # This is a dummy element
        )
    finally:
        try:
            print(type(elem))
            print(elem.get_attribute('innerHTML'))
        except:
            print('print error')
        app_tags.append(elem.get_attribute('innerHTML'))
    # app_tag = driver.find_element(By.TAG_NAME, 'application-tags')


# %%
for app_tag in app_tags:
    print(app_tag)
# ok, save these html to datalake
