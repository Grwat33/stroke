from splinter import Browser
import pandas as pd
from datetime import datetime
import time

def entrylist(gender,age,hypertension,heartdisease,married,worktype,residencetype,bmi,smokingstatus):
    if gender == "male":
        gender = 1
    elif gender == "female":
        gender = 2

    if hypertension == "no":
        hypertension = 0
    elif hypertension == "yes":
        hypertension = 1

    if heartdisease == "no":
        heartdisease = 0
    elif heartdisease == "yes":
        heartdisease = 1

    if married == "no":
        married = 0
    elif married == "yes":
        married = 1

    if worktype == "Govt_job":
        worktype = 1
    elif worktype == "Private":
        worktype = 2
    elif worktype == "Self-employed":
        worktype = 3

    if residence == "Rural":
        worktype = 2
    elif worktype == "Urban":
        worktype = 1

    if smokingstatus == "never":
        smokingstatus = 1
    elif smokingstatus == "formerly":
        smokingstatus = 2
    elif smokingstatus == "smokes":
        smokingstatus = 3

