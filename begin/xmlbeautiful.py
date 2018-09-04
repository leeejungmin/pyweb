from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('http://google.com')

xml = BeautifulSoup(req,'xml')

for item xml.findAll('link')[1:]
    print(item)
    urllib.request.urlopen(url).read()
    print(news)
    print(20*"#")


    #######

import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
# 찾고자하는 디렉토리넣음
course = tree.findall('course/title')

for c in course:
    print(c.text)
#자료를 찾는다
    title = c.find('title').text
    num = c.find('crse').text

    print(' * {} [{}] {}'.format(
            num, days, title
    ))
