from regisProgram import checkBlank, encrypt
from connectDB import connectMongo

def login(username, password):
    if checkBlank(username, password):
        if checkUserPass(username, password):
            if username == "admin":
                return True, "1"
            else:
                return True, "0"
        else:
            print("Wrong Username Or Password")
            return False, ""
    else:
        print("Blank input")
        return False, ""

def checkUserPass(username , password):
    db = connectMongo()
    passEncryp = encrypt(password)
    rs = db.User.find({'User': username})
    for x in rs:
        if x["Pass"] == passEncryp:
            return True
        else:
            return False
