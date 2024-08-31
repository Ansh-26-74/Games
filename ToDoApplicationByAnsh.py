def DisplayMenu(list):
    x = 1
    while(x == 1):
        print("This is the \"To Do Application\"")
        print("1. View To Do List")
        print("2. Add a task")
        print("3. Remove a Task")
        print("4. Mark Task as completed")
        print("5.Exit")

        op = int(input("Select the option: "))
        if(op == 1):
            ViewList(list)
        elif(op == 2):
            AddTask(list)
        elif(op == 3):
            RemoveTask(list)
        elif(op == 4):
            MarkTask(list)
        elif(op == 5):
            x = 0
        else:
            print("Input is invalid")
        if x != 0:
            x = int(input("If you want to continue, type 1; otherwise, type 0: "))


def ViewList(To_Do_List):
    if not To_Do_List:
        print("Empty To Do List")
    else:
        print("To do list is:")
        for i in To_Do_List:
            print(i)

def AddTask(To_Do_List):
    a = 1
    while(a == 1):
        ViewList(To_Do_List)
        task = input("Enter the task to be Added: ")
        To_Do_List.append(task)
        a = int(input("Enter 1 if you want to add more tasks: "))

def RemoveTask(To_Do_List):
    a = 1
    while(a == 1):
        ViewList(To_Do_List)
        delete = input("Enter the task to be deleted: ")
        To_Do_List.remove(delete)
        a = int(input("Enter 1 if you want to mark more tasks completed: "))

def MarkTask(To_Do_List):
    ViewList(To_Do_List)
    a = 1
    while(a == 1):
        s = input("Enter the task to be marked completed: ")
        if(s in To_Do_List):
            index = To_Do_List.index(s)
            To_Do_List[index] = s + " ✓"
            ViewList(To_Do_List)
        else:
            print("Task not present")
        a = int(input("Enter 1 if you want to mark more tasks completed: "))

list = []
DisplayMenu(list)