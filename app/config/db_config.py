# MongoDB Driver async
import os
import motor.motor_asyncio
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASSWORD")
client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://{username}:{password}@databasecluster.1ry5d.mongodb.net/test')
data_base = client.MagangeLifeStyle
product_collection = data_base.products
