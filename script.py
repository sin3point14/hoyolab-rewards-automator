from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 
from webdriver_manager.chrome import ChromeDriverManager
import config
import time

options = webdriver.ChromeOptions()
options.binary_location = config.chrome_location
options.add_argument("--start-maximized")   

browser  = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
browser.get('https://www.hoyolab.com/genshin/accountCenter/')

browser.add_cookie({"name": "account_id", "value": config.account_id, "domain": ".hoyolab.com"})
browser.add_cookie({"name": "ltuid", "value": config.ltuid, "domain": ".hoyolab.com"})
browser.add_cookie({"name": "cookie_token", "value": config.cookie_token, "domain": ".hoyolab.com"})
browser.add_cookie({"name": "ltoken", "value": config.ltoken, "domain": ".hoyolab.com"})

browser.refresh()

time.sleep(10)

browser.find_element_by_class_name('header__avatarwrp').click()
browser.find_element_by_class_name('header__signin').click()
browser.quit()
