from pprint import pprint
from lxml import etree,html
import requests
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


