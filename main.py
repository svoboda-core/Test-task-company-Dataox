import collections
import requests
import datetime
import pymongo
import random
import json
import re
import os
from pymongo import MongoClient
from time import sleep
from bs4 import BeautifulSoup
from bson import json_util, ObjectId


client = pymongo.MongoClient("mongodb+srv://username:password@cluster0.ubdad.mongodb.net/?retryWrites=true&w=majority")

db = client[""] #specify the name of the database
collections = db[""] #specify the database collection

product_info = {}

def get_data(url, page):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
        "sec-ch-ua":'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    try:
        print("Start processing ===> " + page)
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        all_items = soup.find_all("div", {"data-listing-id":re.compile("\d")})

        for item in all_items:
            img = item.find(class_="image").find("img").get("data-src")
            title = item.find("div", class_="title").text.strip()
            title_url = "https://www.kijiji.ca/" + str(item.find("a", class_="title").get("href"))
            date = item.find(class_="date-posted").text.strip().split(" ")[0]
            if date == "<":
                date = str(datetime.datetime.now())
                date_convert = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
                date = datetime.datetime.strftime(date_convert, '%d-%m-%Y')
            else:
                date = date.replace("/", '-')

            city = item.find("div", class_="location").find("span").text.strip().split("City of ")[-1]
            bedrooms = item.find("span", class_="bedrooms").text.split("Beds:")[-1].strip()
            description = item.find(class_="description").text.strip().split("...")[0]
            price = item.find(class_="price").text.strip()
            if price == "Please Contact":
                currency = "currency not specified"
                cost = "price not specified"
            else:
                currency = price.replace("$", '$-').split("-")[0]
                cost = price.replace("$", '$-').split("-")[-1]

            product_info = {
                    "Img": img,
                    "Title":title,
                    "Title_URL":title_url,
                    "datePublished": date,
                    "City": city,
                    "Bedrooms": bedrooms,
                    "Description": description,
                    "Price": {
                        "Currency" : currency,
                        "Cost" : cost,
                    },
                }

            collections.insert_one(product_info)

        print("Finishing processing ===> " + page)

        next_url = soup.find("a", {"title": "Next"})
        if next_url:
            next_url = soup.find("a", {"title": "Next"}).get("href")
            page = next_url.split("/")[-2]
            sleep(random.randrange(4, 6))
            get_data("https://www.kijiji.ca"+ next_url, page=page)
        else:
            print("All pages processed")
            print("Total pages processed ===>" + str(page.split("-")[-1]))

    except Exception as ex:
        print(ex)

    finally:
        if not os.path.isdir('data'):
            os.makedirs('data')

        product_db = []
        for product in collections.find():
            product_db.append(product)

        product_db_json = json.loads(json_util.dumps(product_db))

        with open(f"data/data_db.json", "a", encoding="utf=8") as file:
            json.dump(product_db_json, file, indent=4, ensure_ascii=False)


def main():
    get_data("https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273", page="page-1")


if __name__ == "__main__":
    main()
