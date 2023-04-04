import random
import datetime
import json
from typing import Union
# from fastapi import FastAPI, Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
    # my_dict =  rand_num_date()x
    name = "usha"
    return "Helloo"

@app.route('/getnum/<num>')
def get_rand_num_date(num: int):
    my_dict =  rand_num_date(num)
    return render_template('index2.html', dict = my_dict)


def rand_num_date(n):
    n = int(n)
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