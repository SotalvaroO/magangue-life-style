from pydantic import BaseModel, Field
#from app.product.models.py_object_id import PyObjectId
from bson import ObjectId


class ProductEntity(BaseModel):
    #id:str
    product_code:str
    
# class ProductEntityDb(ProductEntity):
#     id: PyObjectId = Field(default_factory=str, alias='_id')
    
#     class Config:
#         json_encoders = {ObjectId: str}