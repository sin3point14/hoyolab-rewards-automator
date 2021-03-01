from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import argparse
import config
import time

def chromeDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    browser  = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    return browser

def firefoxDriver():
    options = FirefoxOptions()
    options.add_argument("--headless")
    browser = webdriver.Firefox()
    return browser

def run_script(browser):
    browser.get('https://www.hoyolab.com/genshin/')
    browser.add_cookie({"name": "account_id", "value": config.account_id, "domain": ".hoyolab.com"})
    browser.add_cookie({"name": "ltuid", "value": config.ltuid, "domain": ".hoyolab.com"})
    browser.add_cookie({"name": "cookie_token", "value": config.cookie_token, "domain": ".hoyolab.com"})
    browser.add_cookie({"name": "ltoken", "value": config.ltoken, "domain": ".hoyolab.com"})
    browser.refresh()
    time.sleep(10)
    browser.find_element_by_class_name('header__avatarwrp').click()
    try:
        browser.find_element_by_class_name('header__signin').click()
    except NoSuchElementException:
        print("Element does not exist")
    time.sleep(5)
    browser.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automation tool to cuck mihoyo's stupid gacha tactics")
    parser.add_argument("-F", "--firefox", help="Runs the firefox webdriver.", action="store_true")
    parser.add_argument("-C", "--chrome", help="Runs the chrome webdriver (default webdriver).", action="store_true")
    args = parser.parse_args()

    if args.firefox:
        run_script(firefoxDriver())
    else:
        run_script(chromeDriver())
    
