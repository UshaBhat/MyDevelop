
from  fastapi import FastAPI
import random
import datetime
import pandas as pd
app = FastAPI()
@app.get("/my_first_api")
def randomNum():
   rand_list=[]
   for i in range(5):
        rand_list.append(random.randint(0,100))
   return rand_list
nums = randomNum()
def newDate():
# initializing date
   test_date = datetime.datetime.strptime("01-4-2023", "%d-%m-%Y")
# initializing K
   K = 5
   date_generated = pd.date_range(test_date, periods=K)
   return date_generated
dates = newDate()


dict={}
for i in range(5):
    dict[dates[i].strftime("%d-%m-%Y")] = nums[i]
print(dict)

 









    





