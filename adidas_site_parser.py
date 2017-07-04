
from pprint import pprint
from lxml import etree,html
import requests
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#response = requests.get("http://www.adidas.ru/muzhchiny-krossovki")
doc='./adidas_all.html'#response.content

def get_links_of_goods(path=None,url=None):
    if (path is None) and (url is not None):
        response = requests.get(url)
        doc = response.content
    elif (path is not None) and (url is None):
        with open(path,'r') as f:
            doc = f.read()
    else:
        print('error')
    tree = etree.HTML(doc)
    goods = tree.xpath('//div[@class="product-info-inner-content clearfix with-badges"]//a')
    return [item.get('href') for item in goods]



##TODO - TEST reset_actions()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)

driver.get(get_links_of_goods(url = "http://www.adidas.ru/muzhchiny-krossovki")[0])


wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, '//body[@class="adidas-RU visibleDialog"]')))

actions = webdriver.common.action_chains.ActionChains(driver)
actions.click()
actions.perform()


wait.until(expected_conditions.invisibility_of_element_located(
    (By.XPATH, '//body[@class="adidas-RU visibleDialog"]')))

element = driver.find_element_by_xpath('//div[@class="size-dropdown-block"]')

actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()



wait.until(expected_conditions.presence_of_element_located(#visibiliti doent work?!
    (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))

element = driver.find_element_by_xpath('//span[contains(., "{} ")]'.format('39'))

print(element,element.location, element.size)




actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()
print(2)
wait.until(expected_conditions.invisibility_of_element_located( #str 56!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))

print(1)
element = driver.find_element_by_xpath('//button[@name="add-to-cart-button"]')
actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()
######################################

wait.until(expected_conditions.presence_of_element_located(#visibiliti doent work?!
    (By.XPATH, '//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all dialog_minicartoverlay popup-scale-in"]')))

element = driver.find_element_by_xpath('//a[@data-ci-test-id="checkOutButton"]')
print(element,element.location, element.size)
actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()
##################################################
wait.until(expected_conditions.presence_of_element_located(#visibiliti doent work?!
    (By.XPATH, '//input[@class="textinput firstname  required"]')))

element = driver.find_element_by_xpath("//input[@class='textinput firstname  required']")##работает класс, а не айди!!!!!!!!!! ну почему?!
print(111111111111111)
print()
print(element,element.location, element.size)
element.send_keys("some text")
time.sleep(10)

driver.quit()
