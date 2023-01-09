import pymongo
import base64
from config import OWNER_ID

MONGO_URL = ""
Client = pymongo.MongoClient(MONGO_URL)
Database = Client['PyBot']

ColName = "Alt" + str(OWNER_ID)
AltUser = Database.ColName

