from pprint import pprint
from lxml import etree
doc = './adidas_all.html'
f =open(doc,'r')
doc = f.read()
f.close()
tree = etree.HTML(doc)
result = etree.tostring(tree, pretty_print=True, method="html")
#print(result)
r = tree.xpath('//div[@class="product-info-inner-content clearfix with-badges"]')
pprint(r)
for i in r:
    pprint(etree.tostring(i, pretty_print=True,method="html").decode())


