from requests import get
from bs4 import BeautifulSoup as bs
page = get("http://www.tsetmc.com")
soup = bs(page.content, "html.parser")
rows = soup.find("table").find_all("tr")

#وضعیت بازار:
status = "close" if "بسته" in rows[0].find_all("td")[1].text else "open"

#شاخص کل:
total_index = rows[1].find_all("td")[1].text.split()
#مقدار:
total_index_value = total_index[0]
#تغییرات:
total_index_change = total_index[1]
if(total_index_change[0] == "("):
    total_index_change = '-' + total_index_change[1:-1]

#شاخص کل (هم وزن):
weighted_index = rows[2].find_all("td")[1].text.split()
#مقدار:
weighted_index_value = weighted_index[0]
#تغییرات:
weighted_index_change = weighted_index[1]
if(weighted_index_change[0] == "("):
    weighted_index_change = '-' + weighted_index_change[1:-1]

#ارزش بازار:
total_value = rows[3].find("div").get("title")

#ساعت، تاریخ:
date, time = rows[4].find_all("td")[1].text.split()

#تعداد معاملات:
transactions_count = rows[5].find_all("td")[1].text

#ارزش معاملات:
transactions_value = rows[6].find("div").get("title")

#حجم معاملات:
transactions_volume = rows[7].find("div").get("title")
