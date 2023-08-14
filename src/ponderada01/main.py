from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request): 
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(item_id: int, q: Union[str, None] = None):
    return templates.TemplateResponse("index.html", {"request": request})
