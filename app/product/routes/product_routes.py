from fastapi import APIRouter, HTTPException
from app.product.models.product_entity import ProductEntity, ProductEntityUpdate
from app.product.repositories import product_repository

route = APIRouter(prefix='/product', tags=['Product'])

@route.get('')
async def get_products():
    response = await product_repository.get_all_products()
    return response

@route.get('/{product_code}', response_model=ProductEntity)
async def get_product(product_code: str):
    response  = await product_repository.get_product_by_code(product_code)
    if response:
        return response
    raise HTTPException(404, "There is not product with this code {product_code} / Not Found")

@route.post('', response_model=ProductEntity)
async def create_products(product: ProductEntity):
    product_db = product_repository.get_product_by_code(product.product_code)
    if not product_db:
        response = await product_repository.create_product(product.dict())
        if response:
            return response
        raise HTTPException(400, "Something went wrong / Bad Request")
    raise HTTPException(400, "Duplicated / Bad Request")
    

@route.put('/{product_code}', response_model=ProductEntity)
async def update_product(product_code:str, product: ProductEntityUpdate):
    response = await product_repository.update_product(product_code, product)
    if response:
        return response
    raise HTTPException(404, "There is not product with this code {product_code} / Not Found")

@route.delete('/{product_code}')
async def delete_product(product_code: str):
    response = await product_repository.delete_product(product_code)
    print(response)
    if response:
        return {"message": "Success!"}
    raise HTTPException(404, "There is not product with this code {product_code} / Not Found")