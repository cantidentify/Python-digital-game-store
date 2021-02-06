from connectDB import connectMongo
from datetime import datetime
import random
import string

def randomKey():
    size = 6
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def saveOrder(gamelist, user):
    balance = 0
    time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    id = randomKey()
    for x in gamelist:
        balance = balance + float(x[1])
    saveFormat = {"id": id, "status": "0", "user": user, "game": gamelist, "balance": balance, "time": time}
    saveToDB(saveFormat)
    return True

def saveToDB(data):
    db = connectMongo()
    db.Order.insert_one(data)


