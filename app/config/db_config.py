# MongoDB Driver async

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
data_base = client.MagangeLifeStyle
product_collection = data_base.products
