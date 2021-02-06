import pymongo

def connectMongo():
    client = pymongo.MongoClient("mongodb+srv://atip:class@cluster0-po5pa.mongodb.net/test?retryWrites=true&w=majority")
    db = client.get_database("DigitalGameStore")
    return db
