from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
# # 1. Download web page
url = 'http://dantri.com.vn/'
# conn = urlopen(url)
# # 1.2 Read
# data = conn.read()
# # 1.3 Decode
# html_content = data.decode('utf-8')
# print(html_content)

html_content = urlopen(url).read().decode('utf-8')
# print(html_content)

#  save html to file
# import urllib.request
# urllib.request.urlretrieve(url, "dantri.html")

# f = open('dantri.html', 'wb')
# f.write(html_content)
# f.close()

# 2. Extract ROI (Region of Interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
# find by class
ul = soup.find('ul', 'ul1 ulnew')
# print(ul.prettify())

#  3. Extract data
li_list = ul.find_all('li')

data = []

for li in li_list:
    post = {}
    a = li.h4.a
    post["Title"] = a.string
    post["Link"] = str(url + a['href'])
    data.append(post)
    
pyexcel.save_as(records=data, dest_file_name="dantri-data.xlsx")
 