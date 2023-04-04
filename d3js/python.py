import random
import datetime
import json
from typing import Union
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
app = FastAPI()
origins = [
    #  "http://localhost",
     "http://localhost:8000",
    "http://localhost:5500"
    "null"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def read_root():
    return { "message":"Hello World"}
@app.get("/hello/{name}")
async def say_hello(name:str):
    return {"message": f"Hello {name}"}
@app.get("/getnum/{num}", response_class=HTMLResponse)
async def get_rand_num_date(request: Request,num: int):
    my_dict =  rand_num_date(num)
    return templates.TemplateResponse("index.html", {"request": request,"dict":  my_dict})
    # return rand_num_date(num)
def rand_num_date(n):
    rno = []
    for i in range(n):
        rno.append(random.randint(0,100))
    # date_list = []
    # for _ in range(n):
    #     date = datetime.date( 1, random.randint(0,31))
    #     date_list.append(date)
    dates = []
    start_date = datetime.date.today()
    for i in range(n):
        date = start_date - datetime.timedelta(days=i)
        dates.append(date)
    dates = list(map(str,dates))
    dictionary = dict(zip(dates, rno))
    dictionary = json.dumps(dictionary)
    return dictionary