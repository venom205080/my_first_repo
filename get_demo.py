from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import requests as req

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Register(BaseModel):
    email: str
    password: str

dummy_DB = [{"email": "ram123@gmail.com", "password": "itsasecretpassword"},
            {"email": "mynameis@gmail.com", "password":"angelpriya"}]

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>this is home route nothing is here</h1>"


# path parameters example
@app.get("/users/{id}",response_class=HTMLResponse)
async def get_user(request: Request,id:str):
    URL = "https://jsonplaceholder.typicode.com/users"
    res = req.get(URL).json()
    user_details = res[int(id)-1]
    return templates.TemplateResponse(request=request,name="show_user.html", context={"user": user_details})


@app.post("/register")
async def register_user(user:Register):
    email = user.email
    password = user.password
    return {
        "msg": "we got data succesfully",
        "email": email,
        "password": password,
    }
    

    

# query param example
# @app.get("users")
