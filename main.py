from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get('/')
async def home():
    res = RedirectResponse(url='/docs')
    return res
