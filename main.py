from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.product.routes.product_routes import route

app = FastAPI()

app.include_router(route,prefix='/api')

@app.get('/')
async def home():
    res = RedirectResponse(url='/docs')
    return res
