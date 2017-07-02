from pprint import pprint
from lxml import etree,html
import requests
import time
from selenium import webdriver
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
pprint(get_links_of_goods(path = doc))


driver = webdriver.Firefox()
driver.get(get_links_of_goods(path = doc)[0])

actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_by_offset(100, 100).perform()
time.sleep(1)
actions.click().perform()

element = driver.find_element_by_xpath('//div[@class="size-dropdown-block"]')
actions.move_to_element_with_offset(element, 100,10)
actions.click()
actions.perform()

# element = driver.find_element_by_xpath('//button[@name="add-to-cart-button"]')
# element.click()
# driver.quit()
