from fastapi import APIRouter, HTTPException
from app.product.models.product_entity import ProductEntity
from app.product.repositories import product_repository

route = APIRouter(prefix='/product', tags=['Product'])

@route.get('')
async def get_products():
    response = await product_repository.get_all_products()
    return response

@route.get('/{id}')
async def get_product(product: ProductEntity):
    return 1

@route.post('', response_model=ProductEntity)
async def create_products(product: ProductEntity):
    response = await product_repository.create_product(product.dict())
    print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong / Bad Request")

@route.put('/{id}')
async def update_product(product: ProductEntity):
    return 1

@route.delete('/{id}')
async def delete_product(id: str):
    return 1
