from requests import get
from bs4 import BeautifulSoup

#returns a list of usernames:
#returns an empty list for bad inputs:
def find(user_name, tab="followers"):
    print(f"finding {tab}:")
    results = []
    page_num = 1
    while(True):
        url = f"https://github.com/{user_name}?page={page_num}&tab={tab}"
        page = get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        #each user is in a div element with this class:
        elements = soup.find_all(class_="d-inline-block no-underline mb-1")

        #if this is last page(empty):
        if(not elements):
            break

        #each element has 2 span element that the second one contains user's id:
        for element in elements:
            name = element.find_all("span")[1].text
            results.append(name)

        #logging:
        print(f"page {page_num} done!")

        #next_page:
        page_num += 1

    print("- - - - > END < - - - -\n")
    return results

#replace it with your username:
username = "20kevit"

followers = find(username)
following = find(username, "following")

print("followers: ", len(followers))
print("following: ", len(following))

unfollowers = [person for person in following if(not person in followers)]
fans = [person for person in followers if(not person in following)]

print("people who didn't followed back:")
for person in unfollowers:
    print('\t',person)

print("\npeople followed you, but you didn't follow back:")
for person in fans:
    print('\t',person)
