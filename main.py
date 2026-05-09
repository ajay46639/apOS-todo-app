from datetime import datetime 
import json 
import os 
import sys

if os.path.exists("data"):
    pass
else:
    os.makedirs("data")

try :
    with open("data/data.json", "r") as f :
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    empty = {}
    with open("data/data.json", "w") as  f:
        json.dump(empty,f)
    with open("data/data.json", "r") as f:
        data = json.load(f)
        

def add_task(name):
    task_no = len(data) + 1 
    data[task_no] = {"name" : name , "task_done" : False}
    print(f"Task no.{task_no} Added to list! ")
    with open("data/data.json", "w")  as  f:
        json.dump(data, f)



def update_task(task_number):
    data[f"{task_number}"]["task_done"] = True
    print(f"Task no.{task_number} updated to Done!")
    with open("data/data.json", "w")  as  f:
        json.dump(data, f)


    
def get_all_task():
    with open("data/data.json", "r") as f:
        data = json.load(f)          
    print("\n" +"TODO-LIST".center(50, '-')) 
    topline = "Task No.  " + "Task Name " + " "*25 + "Done "
    print(topline)
    print("-"*50)
    for i in range(1, len(data)+1) :
        key = f"{i}"
        name = data[key]["name"]
        done = data[key]["task_done"]
        line = key.center(10) + name.ljust(35) + str(done)
        print(line)
    print("-"*50 + "\n")
    
def get_specific_task(task_no):
    with open("data/data.json", "r") as f:
        data = json.load(f)
    key = f"{task_no}"
    name = data[key]["name"]
    done  = data[key]["task_done"]
    print("\n" + "="*30)
    print(f" ⁕ Task No. : {task_no}" + f"\n ⁕ Task Name : {name}" + f"\n ⁕ Task Done : {done}")
    print("="*30 + "\n")
    

while True :
    print(">>> Menu: \n1. Add Task \n2. Update Task \n3. List all Task \n4. List one Task ")
    cmd = input("Enter cmd no. from  menu ('Q/q' for quit) --> ")
    
    try :
        cmd_no = int(cmd)
    except ValueError as e :
        if cmd.lower() == "q" :
            sys.exit()
        else:
            print("Invalid Input!")
            continue
    
    else:
        if cmd_no ==  1 :
            task_name = input("Task Name : ")
            add_task(task_name)
        elif cmd_no == 2 :
            try :
                task_no = int(input("Update Task no. : "))
            except ValueError as e :
                print("Invalid Input ! ")
                continue
            update_task(task_no)
            
        elif cmd_no == 3 :
            get_all_task()
        
        elif cmd_no == 4 :
            try:
                task_no = int(input("Enter Task no. : "))
            except ValueError as e :
                print("Invalid Input !")
                continue
            get_specific_task(task_no)
            
        else:
            print("Invalid Input! (cmd not available))")
            continue


with open("data/data.json", "w")  as  f:
    json.dump(data, f)

    
     
    
    
    