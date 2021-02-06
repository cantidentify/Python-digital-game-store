from datetime import datetime
from connectDB import connectMongo

def addGame(*get):
    name = get[0]
    des = get[1]
    price = get[2]
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    data = {"name": name, "des": des, "price": price, "time": time}
    db = connectMongo()
    db.Games.insert_one(data)
    return True

def checkPrice(get):
    try:
        val = int(get)
        if val > 0:
            return True
    except ValueError:
        return False

def checkSameName(get):
    name = get
    db = connectMongo()
    rs = db.Games.find({'name': name})
    for x in rs:
        if name == x['name']:
            return False
    return True

