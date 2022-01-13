from requests import get
from bs4 import BeautifulSoup as bs
page = get("http://www.tsetmc.com")
soup = bs(page.content, "html.parser")
rows = soup.find("table").find_all("tr")
for i in range(len(rows)):
    data = rows[i].find_all("td")
    rows[i][0] = data[0].text
    rows[i][1] = data[1].text
    
for i in rows:
    print(i[0])
    print(i[1])
    print('\n')
	
#result will be like:
"""
وضعیت بازار
بسته 

شاخص کل
1,334,265 (439.12)

شاخص كل (هم وزن)
353,768.49 355.89

ارزش بازار
53,475,011.039 B

اطلاعات قیمت
00/10/22 17:34:21

تعداد معاملات
325,678

ارزش معاملات
24,845.918 B

حجم معاملات
4.226 B
"""
