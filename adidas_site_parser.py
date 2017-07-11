from pprint import pprint
from lxml import etree,html
import requests
import time
import sys

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

doc='./adidas_all.html'


def progressbar_dec(function_to_decorate):
    def ppb(i, l):#PrintProgressbar
        printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    return ppb


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


def get_links_of_goods(url,key_word):
    if (url is not None):
        response = requests.get(url)
        doc = response.content
    else:
        print('error')

    tree = etree.HTML(doc)
    goods = tree.xpath('//div[@class="product-info-inner-content clearfix with-badges"]//a')
    return [item.get('href') for item in goods if  key_word.lower() in item.get('data-productname').lower()]

def place_order(size,link):

    l = 18
    ppb = progressbar_dec(printProgressBar)

    i = 0
    ppb(i,l)

    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)
    driver.get(link)

    i+=1
    ppb(i,l)

    wait.until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//body[@class="adidas-RU visibleDialog"]')))

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)

    wait.until(expected_conditions.invisibility_of_element_located(
        (By.XPATH, '//body[@class="adidas-RU visibleDialog"]')))

    element = driver.find_element_by_xpath('//div[@class="size-dropdown-block"]')

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)

    wait.until(expected_conditions.presence_of_element_located(#visibiliti doent work?!
        (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))

    element = driver.find_element_by_xpath('//span[contains(., "{} ")]'.format(size))

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)

    wait.until(expected_conditions.invisibility_of_element_located(
         (By.XPATH, '//div[@class="ffSelectMenuWrapper"]')))


    element = driver.find_element_by_xpath('//button[@name="add-to-cart-button"]')

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)


    wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//div[@class="ui-dialog ui-widget ui-widget-content ui-corner-all dialog_minicartoverlay popup-scale-in"]')))

    element = driver.find_element_by_xpath('//a[@data-ci-test-id="checkOutButton"]')

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)

    wait.until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//input[@class="textinput firstname  required"]')))

    i+=1
    ppb(i,l)

    data = {
        "//input[@class='textinput firstname  required']": "firstname",
        "//input[@class='textinput lastname  required']" : "lastname",
        "//input[@class='textinput city  required']" : "Moscow",
        "//input[@class='textinput zip  required']" : "116410",
        "//input[@class='textinput address1  required']" : "address1",
        "//input[@class='textinput housenumber  required']" : "15",
        "//input[@class='textinput apartmentnumber ']" : '15'
    }

    for xpath, value in data.items():
        driver.find_element_by_xpath(xpath).send_keys(value)
        i+=1
        ppb(i,l)

    element = driver.find_element_by_xpath('//input[@data-ci-test-id=\'phoneField\']')

    element.location_once_scrolled_into_view
    element.send_keys("9898998898")

    i+=1
    ppb(i,l)

    element = driver.find_element_by_xpath('//*[@id="dwfrm_delivery"]/div[2]/div[3]/div[2]/div[2]/div[1]/div/div/div')

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)

    element = driver.find_element_by_xpath("//input[@data-ci-test-id='eMailField']")
    element.send_keys("emil@mail.ru")

    i+=1
    ppb(i,l)

    element = driver.find_element_by_xpath('//button[@id="dwfrm_delivery_savedelivery"]')

    element.location_once_scrolled_into_view

    actions = webdriver.common.action_chains.ActionChains(driver)
    actions.move_to_element(element)
    actions.click()
    actions.perform()

    i+=1
    ppb(i,l)
    #time.sleep(10)
    driver.quit()

for link in get_links_of_goods('http://www.adidas.ru/muzhchiny-krossovki', sys.argv[2]):
    place_order(sys.argv[1],link)
