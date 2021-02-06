from connectDB import connectMongo

def callData():
    db = connectMongo()
    rs = db.Games.find({})
    count = db.Games.count_documents({})
    data = []
    index = []
    for x in rs:
        index.append(x["name"])
        index.append(x["des"])
        index.append(x["price"])
        index.append(x["time"])
        data.append(index)
        index = []
    return data, count

def callDataForOrder(choice):
    db = connectMongo()
    if choice != "0":
        if choice == "1":
            rs = db.Order.find({"status": "1"})
        else:
            rs = db.Order.find({"status": "0"})
    else:
        rs = db.Order.find({})
    count = db.Order.count_documents({})
    uselater = []
    data = []
    index = []
    index2 = []
    for x in rs:
        index.append(x["id"])
        index.append(x["user"])
        index.append(str(x["balance"]))
        if x["status"] == '0':
            index.append("Waiting")
        else:
            index.append("Approved")
        data.append(index)
        index = []

        index2.append(x["id"])
        index2.append(x["user"])
        index2.append(str(x["balance"]))
        if x["status"] == '0':
            index2.append("Waiting")
        else:
            index2.append("Approved")

        index2.append(x["game"])
        index2.append(x["time"])
        uselater.append(index2)
        index2 = []
    return data, count, uselater

