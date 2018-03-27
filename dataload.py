from random import randint
from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017")
db = client['myRetail']
coll = db['products']
currency_code_list = ["USD", "INR", "EUR", "JPY", "AUD", "NZD"]


def readFile():
    return open('product_names.txt').read().splitlines();

for i in readFile():
    request = coll.insert_one(
        {
            "id": randint(9999999, 99999999),
            "name": random.choice(readFile()),
            "current_price": {
                "value": round(random.uniform(0.00, 100.00), 2),
                "currency_code": random.choice(currency_code_list)
            }
        }
    )
    print("Inserted Document ======>> "+str(request))


