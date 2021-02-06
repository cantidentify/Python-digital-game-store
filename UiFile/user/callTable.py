from connectDB import connectMongo

def callData(user):
    db = connectMongo()
    rs = db.Order.find({'$and': [{'status': '0'}, {'user': '{0}'.format(user)}]})
    count = db.Order.count_documents({})
    if count > 0:
        data = []
        index = []
        data2 = []
        index2 = []
        for x in rs:
            index.append(x["id"])
            index.append(str(x["balance"]))
            data.append(index)
            index = []

            index2.append(x["id"])
            index2.append(str(x["balance"]))
            index2.append(x["game"])
            index2.append(x["time"])
            data2.append(index2)
            index2 = []
        return data, 1, data2
    else:
        return [], 0
