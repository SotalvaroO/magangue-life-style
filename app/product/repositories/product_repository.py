from app.config.db_config import product_collection
from app.product.models.product_entity import ProductEntity, ProductEntityUpdate


async def get_product_by_code(code: str):
    document = await product_collection.find_one({"product_code": code})
    return document
    # return ProductEntity(**document)


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


async def update_product(product_code: str, product: ProductEntityUpdate):
    await product_collection.update_one(
        {"product_code": product_code},
        {"$set": product.dict(exclude_unset=True)})
    document = await product_collection.find_one({"product_code": product_code})
    return document

async def delete_product(product_code: str):
    response = await product_collection.delete_one({"product_code": product_code})
    if response.deleted_count == 1:
        return True
    return False