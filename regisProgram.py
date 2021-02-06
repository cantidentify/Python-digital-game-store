from connectDB import connectMongo
import re
import hashlib

def checkBlank(*get):
    for x in get:
        if x == "":
            return False
    return True

def checkSameUser(user, email):
    user = user.strip()
    email = email.strip()
    db = connectMongo()
    rs = db.User.find({'User': user})
    for x in rs:
        if user == x['User'] or email == x['Email']:
            return False
    return True

def checkPassword(password):
    password = password.strip()
    if len(password) <= 4:
        return False
    return True

def checkEmail(email):
    pattern = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    email = email.strip()
    if re.search(pattern, email):
        return True
    else:
        return False

def encrypt(password):
    data = password.strip()
    return (hashlib.md5(data.encode()).hexdigest())

def saveToDB(username, password, email):
    username = username.strip()
    password = password.strip()
    password = encrypt(password)
    email = email.strip()
    data = {"User": username, "Pass": password, "Email": email}
    db = connectMongo()
    rs = db.User.insert_one(data)