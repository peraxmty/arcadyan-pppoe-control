#!/usr/bin/python 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()  
chrome_options.add_argument("--headless") 

browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('http://192.168.200.254')

element =  browser.find_element_by_name('pws')
element.send_keys("PASSWORD")
element.send_keys(Keys.ENTER)

browser.implicitly_wait(20)

frameInf = browser.find_element_by_xpath('/html/frameset/frame[2]')
browser.switch_to.frame(frameInf)

frameIzq = browser.find_element_by_xpath('//*[@id="leftFrame"]')
browser.switch_to.frame(frameIzq)

wan = browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[4]/td/table[1]/tbody/tr/td/span')
wan.click()

pppoe = browser.find_element_by_xpath('//*[@id="wan"]/tbody/tr/td/span')
pppoe.click()

browser.switch_to_default_content()
frameInf = browser.find_element_by_xpath('/html/frameset/frame[2]')

browser.switch_to.frame(frameInf)

frameDerecho = browser.find_element_by_xpath('//*[@id="main2"]')
browser.switch_to.frame(frameDerecho)

usuario = browser.find_element_by_name('ISP_Username')
usuario.send_keys('x')

aplicar = browser.find_element_by_xpath('/html/body/form/table[3]/tbody/tr/td/input[1]')
aplicar.click()
time.sleep(10)

browser.switch_to_default_content()
frame = browser.find_element_by_xpath('/html/frameset/frame[1]')
browser.switch_to.frame(frame)

element = browser.find_element_by_name('Image2')
element.click()

browser.implicitly_wait(20)
browser.switch_to_default_content()
element =  browser.find_element_by_name('pws')
browser.quit()
