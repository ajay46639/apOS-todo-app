from datetime import datetime 
import json 
import os 

if os.path.exists("data"):
    pass
else:
    os.makedirs("data")

try :
    with open("data/data.json", "r") as f :
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    empty = {}
    with open("data/data.json", "w+") as  f:
        json.dump(empty,f)

data = empty

def add_task(name):
    task_no = len(data) + 1 
    data[task_no] = {"name" : name , "task_done" : False}
    print(f"Task no.{task_no} Added to list! ")


def update_task(task_number):
    data[task_number]["task_done"] = True 
    print(f"Task no.{task_number} updated to Done!")

    
    
def get_all_task():
    for i in range(1, len(data)+1) :
        print(f"{i} : {data[i].items()}")

def get_specific_task(task_no):
    print(data[task_no])

add_task("running at 6 am")
add_task("piano at 8 am ")
add_task("gym at 7 am ")
update_task(3)

with open("data/data.json", "w")  as  f:
    json.dump(data, f)

with open("data/data.json", "r") as f:
    load = json.load(f)

print(load["2"]["name"])
print(load["3"]["task_done"])

    
    
    
    
    