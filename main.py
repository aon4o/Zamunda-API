from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

import models
from database import engine
from routers import users, torrents, admin

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.include_router(admin.router)
app.include_router(users.router)
app.include_router(torrents.router)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
