from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
html_content = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html_content, 'html.parser')

# danh dau ROI & tao list cho data:
roi_data = soup.find('table', {'id':"tableContent"})
tr_list = roi_data.find_all('tr', {"class": ["r_item ", "r_item_a "]})
data = []

# danh dau ROI & tao list cho ten cot:
roi_col_name = soup.find('div', {'id':'divTableHeader'})
a = roi_col_name.find_all('td', 'h_t')
col_name_list = ["Danh mục"]
for i in range (len(a)):
    col_name = a[i].text.strip()
    col_name_list.append(col_name)

# extract data:
for tr in tr_list:
    col={}
    for j in range (len(col_name_list)):
        if j == 0:
            col0 = tr.find('td', {'style': ["width:32%;color:#014377;", "width:32%;color:#014377;font-weight:bold;","width:32%;color:#014377;font-style:italic;"]})
            col[col_name_list[j]] = col0.text.strip()
        elif j == 1:
            col1 = tr.find('td', {'style': ["width:15%;padding:4px;color:#014377;font-weight:bold;","width:15%;padding:4px;color:#014377;","width:15%;padding:4px;color:#014377;font-style:italic;"]})
            col[col_name_list[j]] = col1.string   
        else:
            col_previous = col1
            for k in range (len(col_name_list)-2):
                col_next = col_previous.find_next('td', {'style': ["width:15%;padding:4px;color:#014377;font-weight:bold;","width:15%;padding:4px;color:#014377;","width:15%;padding:4px;color:#014377;font-style:italic;"]})
                col[col_name_list[j]] = col_next.string
                col_previous = col_next
    
    data.append(col)

# save ra file excel:
pyexcel.save_as(records=data, dest_file_name="CafeF-table.xlsx")
