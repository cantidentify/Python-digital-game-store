from connectDB import connectMongo

def deleteProgram(name):
    db = connectMongo()
    rs = db.Games.delete_one({'name': '{0}'.format(name)})
    if rs.deleted_count == 1:
        return True
    else:
        return False

def callFromName(name):
    db = connectMongo()
    rs = db.Games.find({"name": "{0}".format(name)})
    for x in rs:
        return x



def updateGame(nameid, des, price):
    db = connectMongo()
    myquery = {"name": "{0}".format(nameid)}
    newvalues = {"$set": {"des": "{0}".format(des), "price": "{0}".format(price)}}
    rs = db.Games.update_one(myquery, newvalues)
    count = rs.modified_count
    return count