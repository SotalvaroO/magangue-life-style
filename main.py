from itertools import product
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.product.routes import product_routes

app = FastAPI()
app.include_router(product_routes.route)

@app.get('/')
async def home():
    res = RedirectResponse(url='/docs')
    return res
