#! python3
# Preenchendo formulários com Selenium.

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://gmail.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()

# browser = webdriver.Firefox()
# browser.get('https://200.136.54.26')
# emailElem = browser.find_element_by_id('username')
# emailElem.send_keys('admin')
# passwordElem = browser.find_element_by_id('password')
# passwordElem.send_keys('11234')
# passwordElem.submit()

