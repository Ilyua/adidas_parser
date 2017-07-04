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


wait.until(expected_conditions.visibility_of_element_located(#ждать до тех пор пока не станет видим
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

wait.until(expected_conditions.presence_of_element_located(#ГОСПОДИ, ЧТО? visibiliti doent work?!
    (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))

element = driver.find_element_by_xpath('//span[contains(., "{} ")]'.format('39'))

print(element,element.location, element.size)




actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()

# wait.until(expected_conditions.visibility_of_element_located(
#     (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))
# time.sleep(1)
# element = driver.find_element_by_xpath('//button[@name="add-to-cart-button"]')
# element.click()
time.sleep(10)

driver.quit()
