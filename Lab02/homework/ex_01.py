from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'
html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')
sec = soup.find('section', 'section chart-grid')

li_list = sec.find_all('li')

data = []

for li in li_list:
    post = {}
    post["Name"] = li.h3.string
    post["Artist"] = li.h4.string
    data.append(post)

# save excel files consisting of names and artist
pyexcel.save_as(records=data, dest_file_name="iTunes-Top-Songs.xlsx")

# download all youtube videos
querries = []
for post in data:
    querry = "'" + post["Name"] + " " + post ["Artist"] + "'"
    querries.append(querry)

for i in range (len(querries)):
    options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
    }
    dl = YoutubeDL(options)
    dl.download([querries[i]])
