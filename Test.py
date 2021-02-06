from connectDB import connectMongo
from regisProgram import checkSameUser
import re

#db = connectMongo()

# data = {"User": "Test", "Pass": "1234"}
# rs = db.User.insert_one(data)

#checkSameUser("Test")

pattern = 'aab*'
email = "v"
if re.search(pattern, email):
    print("")
else:
    print("invalid")