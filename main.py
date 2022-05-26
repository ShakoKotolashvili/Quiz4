import requests
from bs4 import BeautifulSoup
file = open("result.csv", "w", encoding="utf-8_sig")
base_url = 'https://top.ge/page/'


for page in range(1, 6):

    r = requests.get(base_url + str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    table_data = soup.find("tbody")

    rows = table_data.find_all("tr")

    file.write("სათაური" + "," + "აღწერა" + "," + "საშუალო მომხმარებელი დღეში\n")

    for item in rows:

        columns = item.find_all("td")

        titles = columns[2].find_all("a")
        description = columns[4].text
        average_stats = columns[-4].find("span")

        print(titles[0].text, "- აღწერა: " + description, f"({titles[1].text.strip()})", f"- {average_stats.text}")
        file.write(f"{titles[0].text},{description},{average_stats.text}" + "\n")

file.close()