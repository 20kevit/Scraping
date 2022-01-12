from requests import get
from bs4 import BeautifulSoup


file = open("file_path", "w")

#counting number of coins
num = 0

#Because there is 90 pages for scraping:
for page_num in range(1, 91):
    #logging:
    print("page: ", page_num, " Done.")
	
    #downloade page:
    page = get(f"https://coinmarketcap.com/?page={page_num}")
    soup = BeautifulSoup(page.content, 'html.parser')
	
    #there is 100 coin in each page
    #each coin is in a <tr> element
    #firts one is not what we need
    rows = soup.find_all("tr")[1:]
	
    #the first 10 coins in each page is in different way:
    for i in range(10):
		num += 1
        try:
	    #link will be like this: '/currencies/bitcoin/'
            link = rows[i].find("a").get("href")
			
	    #coin's full name, e.g: bitcoin
            name = rows[i].find_all("p")[1].text
			
	    #write data on file:
            file.write(f"{num} > {name} , {link}\n")
			
        except:
	    #logging:
            print(f"error in page {page_num}, index:{i}")
	
    #next 90 coins a little bit different:
    for i in range(10, 100):
		num += 1
        try:
            td = rows[i].find_all("td", limit=3)[2]
            link = td.find("a").get("href")
            name = td.find_all("span", limit=2)[1].text
            file.write(f"{num} , {name} , {link}\n")
        except:
            print(f"error in page {page_num}, index:{i}")

file.close()
