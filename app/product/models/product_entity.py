from pydantic import BaseModel  # , Field
from typing import Optional
#from app.product.models.py_object_id import PyObjectId
#from bson import ObjectId


class ProductEntity(BaseModel):
    # id:str
    product_code: str
    product_name: str
    product_category: str
    product_price: int

# class ProductEntityDb(ProductEntity):
#     id: PyObjectId = Field(default_factory=str, alias='_id')

#     class Config:
#         json_encoders = {ObjectId: str}


class ProductEntityUpdate(BaseModel):
    product_name: Optional[str]
    product_category: Optional[str]
    product_price: Optional[int]
