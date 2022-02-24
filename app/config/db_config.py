# MongoDB Driver async
from decouple import config
import motor.motor_asyncio
import os

#url: str = config('MONGO_URL')
url: str = os.getenv('MONGO_URL')
client = motor.motor_asyncio.AsyncIOMotorClient(url)
data_base = client.MagangeLifeStyle
product_collection = data_base.products
