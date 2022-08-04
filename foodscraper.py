# import required modules
from bs4 import BeautifulSoup
import requests
import json
 
# get URL
page = requests.get("https://en.wikipedia.org/wiki/List_of_fast-food_chains_in_Canada")
 
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()
list(soup.children)


places = soup.find_all('div', class_='div-col')[0]
#print(places.text)




placeStr = []
for place in places:
    placeStr.append(place.text.split('\n'))
placeStr.remove(placeStr[0])
placeStr.remove(placeStr[-1])
#print(placeStr)


res_list = []

for i in range(len(placeStr[0])):
    res_list.append(placeStr[0][i])
jsonStr = json.dumps(placeStr, indent=4)

# print(res_list)
# print(jsonStr)


#write to a json file
with open('food.json', 'w') as f:
    json.dump(placeStr, f)

