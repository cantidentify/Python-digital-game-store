from connectDB import connectMongo
import smtplib
import random
import string

def codeGenerate():
    size = 10
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def findEmail(name):
    db = connectMongo()
    rs = db.User.find({"User": "{0}".format(name)})
    email = ""
    for x in rs:
        email = x["Email"]
    return email

def sentEmail(infoTosend, gamelist, admin):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        emailtosend = findEmail(admin)
        emailtoreceive = findEmail(infoTosend[1])
        smtp.login("pythongamestore@gmail.com", "dupjjghmdkbkdojn")
        subject = "{0}, Thank you for buying the game from our store".format(infoTosend[1])
        body = "The list of the game of your order number : [{0}]\n".format(infoTosend[0])
        count = 1
        for x in gamelist:
            body = body + "{0}) {1:20}Activation code is    [{2}]\n".format(count, x[0], codeGenerate())
            count = count + 1
        msg = f'Subject: {subject}\n\n{body}'
        smtp.sendmail("{0}".format(emailtosend), "{0}".format(emailtoreceive), msg)

def approveProcess(orderID, infoTosend, gamelist, username):
    db = connectMongo()
    rs = db.Order.update_one({"id": orderID}, {"$set": {"status": "1"}})
    if rs.modified_count == 1:
        sentEmail(infoTosend, gamelist, username)
        return True
    return False