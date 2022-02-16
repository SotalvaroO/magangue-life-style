from app.config.db_config import product_collection
from app.product.models.product_entity import ProductEntity

async def get_product_by_id(code:str):
    document = await product_collection.find_one({"product_code":code})
    return document
    #return ProductEntity(**document)

async def get_all_products():
    products = []
    cursor = product_collection.find({})
    async for document in cursor:
        products.append(ProductEntity(**document))
    return products

async def create_product(product):
    document = product
    result = await product_collection.insert_one(document)
    return document