import pymongo

def connectDB():
    client = pymongo.MongoClient("mongodb+srv://atip:class@cluster0-po5pa.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("Practice")
    return db

def getResult():
    data = []
    db = connectDB()
    rs = db.Club.find({'City': 'Liverpool'})
    for x in rs:
        data.append(x)
    return data

if __name__ == '__main__':
    getData()
