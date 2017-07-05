
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

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

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
i = 0
l = 10
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)
driver.get(get_links_of_goods(url = "http://www.adidas.ru/muzhchiny-krossovki")[0])
i+=1
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)


wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, '//body[@class="adidas-RU visibleDialog"]')))


#driver.get(get_links_of_goods(url = "http://www.adidas.ru/muzhchiny-krossovki")[0])
print(1)

wait.until(expected_conditions.visibility_of_element_located(
    (By.XPATH, '//body[@class="adidas-RU visibleDialog"]')))
print(2)
actions = webdriver.common.action_chains.ActionChains(driver)
actions.click()
actions.perform()

i+=1
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

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


i+=1
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()
print(2)
wait.until(expected_conditions.invisibility_of_element_located( #str 56!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))

print(1)
i+=1
printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

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
element.send_keys("some text")

# data = {
#     "//input[@class='textinput firstname  required']": 'lastname'
# }

# for xpath, value in data.items():
#     driver.find_element_by_xpath(xpath).send_keys(value)

driver.find_element_by_xpath("//input[@class='textinput firstname  required']").send_keys("firstname")
element = driver.find_element_by_xpath("//input[@class='textinput lastname  required']").send_keys("lastname")
element = driver.find_element_by_xpath("//input[@class='textinput city  required']")##работает класс, а не айди!!!!!!!!!! ну почему?!
element.send_keys("city")
element = driver.find_element_by_xpath("//input[@class='textinput zip  required']")##работает класс, а не айди!!!!!!!!!! ну почему?!
element.send_keys("115409")
element = driver.find_element_by_xpath("//input[@class='textinput address1  required']")##работает класс, а не айди!!!!!!!!!! ну почему?!
element.send_keys("address1")
element = driver.find_element_by_xpath("//input[@class='textinput housenumber  required']")##работает класс, а не айди!!!!!!!!!! ну почему?!
element.send_keys("housenumber")
element = driver.find_element_by_xpath("//input[@class='textinput apartmentnumber ']")##работает класс, а не айди!!!!!!!!!! ну почему?!
element.send_keys("apartment")
time.sleep(1)


element = driver.find_element_by_xpath('//input[@data-ci-test-id=\'phoneField\']')


#    element = driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone']")##работает класс, а не айди!!!!!!!!!! ну почему?!
print(element,element.location, element.size)
time.sleep(5)
actions = webdriver.common.action_chains.ActionChains(driver)
element.location_once_scrolled_into_view
# actions.move_to_element(element)
# actions.click()
# actions.perform()
# action.key_down(Keys.CONTROL).perform()
# action.key_up(Keys.CONTROL).perform()
element.send_keys("989)899-88-98")

element = driver.find_element_by_xpath('//*[@id="dwfrm_delivery"]/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/div')
actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()

actions.perform()
print(element,element.location, element.size)

time.sleep(1)
element = driver.find_element_by_xpath("//input[@data-ci-test-id='eMailField']")##работает класс, а не айди!!!!!!!!!! ну почему?!
element.send_keys("emil@mail.ru")

element = driver.find_element_by_xpath('//button[@id="dwfrm_delivery_savedelivery"]')
element.location_once_scrolled_into_view
actions = webdriver.common.action_chains.ActionChains(driver)
actions.move_to_element(element)
actions.click()
actions.perform()
print(element,element.location, element.size)
time.sleep(10)

driver.quit()
