# MongoDB Driver async
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://<username>:<password>@databasecluster.1ry5d.mongodb.net/test')
data_base = client.MagangeLifeStyle
product_collection = data_base.products
