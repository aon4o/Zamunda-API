from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

from database import Base, engine
from models import user, category, sub_category, torrent
from routers import users, torrents, admin, categories, sub_categories

templates = Jinja2Templates(directory="templates")

app = FastAPI()


@app.on_event("startup")
def startup_event():
    # Move the create_all call to the startup event
    Base.metadata.create_all(bind=engine, tables=[
        user.User.__table__,
        category.Category.__table__,
        sub_category.SubCategory.__table__,
        torrent.Torrent.__table__,
    ])


app.include_router(admin.router)
app.include_router(categories.router)
app.include_router(sub_categories.router)
app.include_router(torrents.router)
app.include_router(users.router)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
