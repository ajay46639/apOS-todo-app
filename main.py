from datetime import datetime 
import json 
import os 
import sys

os.system("cls")

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


def load():
    with open("data/data.json", "r") as f :
        data = json.load(f)
def save():
    with open("data/data.json", "w") as f :
        json.dump(data, f)
        



def add_task(name):
    task_no = len(data) + 1 
    data[task_no] = {"name" : name , "task_done" : False}
    save()
    print(Fore.GREEN + f"Task no.{task_no} Added to list! ")


def update_task(task_number):
    key = str(task_number)
    data[key]["task_done"] = True
    save()
    print(f"Task no.{task_number} updated to Done!\n")

    
def get_all_task():
    load()
    print("\n" +"TODO-LIST".center(50, '-')) 
    topline = "Task No.  " + "Task Name " + " "*25 + "Done "
    print(topline)
    print("-"*50)
    for i in range(1, len(data)+1) :
        key = str(i)
        name = data[key]["name"]
        done = data[key]["task_done"]
        line = key.center(10) + name.ljust(35) + str(done)
        print(line)
    print("-"*50 )
    
    
def get_specific_task(task_no):
    load()
    key = str(task_no)
    name = data[key]["name"]
    done  = data[key]["task_done"]
    print("\n" + "="*30)
    print(f" ⁕ Task No.  : {task_no}" + f"\n ⁕ Task Name : {name}" + f"\n ⁕ Task Done : {done}")
    print("="*30 + "\n")

    
def resort():
    values = list(data.values())
    data.clear()
    for i,task in enumerate(values, 1) :
        data[str(i)] = task
    save()
    
    
def remove_task(task_no):
    load()
    removed_task = data.pop(str(task_no))
    print(f"Task '{removed_task["name"]}' Removed !\n")
    resort()
    save()
    
def edit_task(task_no, new_name, task_status = False):
    load()
    data[str(task_no)]["name"] = new_name
    if task_status:
        data[str(task_no)]["task_done"] = not data[str(task_no)]["task_done"]
    save()
    print("Task Edited Successfully >>> ")
    get_specific_task(task_no)
    

menu = "\n>>> Menu : \n1. Add Task \n2. Update Task Status \n3. List all Task \n4. List one Task \n5. Remove Task \n6. Edit Task\n"
print(menu)

while True :
    cmd = input("\nEnter cmd no. from menu :  \n> 'Q/q' for quit\n> 'M/m' for menu \n---------> ")
    
    try :
        cmd_no = int(cmd)
    except ValueError as e :
        if cmd.lower() == "q" :
            sys.exit()
        elif cmd.lower() == "m" :
            print(menu)
            continue
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
            
            try :
                get_specific_task(task_no)
            except KeyError as e :
                print("Invalid Input (Task not Exist!)")
                continue
                
        
        elif cmd_no == 5 :
            try :
                task_no = int(input("Enter Task no. : "))
            except ValueError as e :
                print("Invalid Input !")
                continue
                
            try :
                remove_task(task_no)
            except KeyError as e :
                print("Invalid Input (Task not Exist!)")
                continue    
                
        
        elif cmd_no == 6 :
            try :
                task_no = int(input("Enter Task no. : "))
            except ValueError as e :
                print("Invalid Input !")
                continue
            
            try :
                get_specific_task(task_no)
            except KeyError as e :
                print("Invalid Input (Task not Exist!)")
                continue
            else:    
                print("You want to edit above Task > ")
                new_name = input("\nEnter new Task : ")
                task_status = input("\nWant to edit task Status (y/n): ")
                if task_status.lower() == "y" :
                    edit_task(task_no, new_name, True)
                else :
                    edit_task(task_no, new_name)
                
            
        else:
            print("Invalid Input! (cmd not available))")
            continue


save()
    
     
    
    
    