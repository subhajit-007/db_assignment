from config import DB_INSTANCE


def set_priority(priority_num):
    """ Returns priority parameter as a string """
    match priority_num:
        case 0:
            return "Low"
        case 1:
            return "Mid"
        case 2:
            return "High"
        case _:
            return "None"


def check_task_name(task_name):
    """ Check for empty task name provided by user """
    if len(task_name.strip()) > 0:
        return task_name.strip()
    else:
        raise ValueError("Task name can not be empty!!")


def check_priority(priority_value):
    """ Check for priority before saving into DB """
    if priority_value in [0, 1, 2]:
        return priority_value
    else:
        raise ValueError("Priority value not found!!")


def list_task():
    """ prints list of task with their priority """
    count = 0
    records = DB_INSTANCE.task.estimated_document_count()
    if records > 0:
        print("--------------------")
        print(f"\tTotal Tasks: {records}")
        print("--------------------")
        for task in DB_INSTANCE.task.find():
            count += 1
            task_info = f"{count}. {task.get('task')} - Priority {set_priority(int(task.get('task_priority')))}"
            print(task_info)
        print("--------------------")
    else:
        print("-----No task found-----")


def add_task():
    """ Add new task into the database """
    task_name = check_task_name(input("\nEnter task name: "))
    priority_options = '''
    Choose priority: 
    1. High
    2. Moderate
    3. Low
    '''
    task_priority = int(input(priority_options))

    # priority values => 0: low; 1: mid; 2: high
    entry = {
        "task": task_name,
        "task_priority": check_priority((task_priority - 3) * -1)
    }

    task_added = DB_INSTANCE.task.insert_one(entry)
    if task_added.acknowledged:
        print("\n-----Task added successfully!!-----")
    else:
        print("\n-----Task not added!! Try again!!-----")


def update_task():
    """ This will update the selected task"""
    task_name_to_update = check_task_name(input("\nEnter task name to update ?\n=>"))
    priority_options = '''
    Choose priority: 
    1. High
    2. Moderate
    3. Low
    '''
    task_found = DB_INSTANCE.task.find_one({"task": task_name_to_update})
    if task_found:
        updated_name = check_task_name(input("\nEnter new task name ?\n=>"))
        print(f"\n-----Current Priority is - {set_priority(int(task_found.get('task_priority')))}-----")
        updated_priority = check_priority((int(input(priority_options)) - 3) * -1)
        filters = {"task": task_name_to_update}
        task_updated = DB_INSTANCE.task.update_one(
            filters, {"$set": {"task": updated_name, "task_priority": updated_priority}}
        )
        if task_updated.acknowledged:
            print("\n-----Task updated successfully!!-----")
        else:
            print("\n-----Task not updated!! Try again!!-----")
    else:
        print("-----Task name not found!! Plz try again!!-----")


def delete_task():
    """ This will delete the selected task"""
    task_name_to_delete = check_task_name(input("\nEnter task name to delete ?\n=>"))
    task_found = DB_INSTANCE.task.find_one({"task": task_name_to_delete})
    if task_found:
        query = {"task": task_name_to_delete}
        deleted_task = DB_INSTANCE.task.delete_one(query)
        print(f"----- {deleted_task.deleted_count} task deleted!! -----")
    else:
        print("-----Task name not found!! Plz try again!!-----")


def delete_all_task():
    """ This will delete all tasks"""
    delete_confirmation = input("\nAre you sure to delete all the tasks ?(Y/N)\n=>")
    if delete_confirmation.lower() == 'y':
        deleted_task = DB_INSTANCE.task.delete_many({})
        print(f"----- {deleted_task.deleted_count} tasks deleted!! -----")


def main():
    """ Main menu of the application """
    options = '''
    Choose option: 
    1. Add Task
    2. Update Task
    3. List Task
    4. Delete Task
    5. Delete All Task
    6. Exit
    '''

    user_input = int(input(options))  # todo: handle type conversion error here

    match user_input:
        case 1:
            add_task()
        case 2:
            update_task()
        case 3:
            list_task()
        case 4:
            delete_task()
        case 5:
            delete_all_task()
        case 6:
            exit(0)
        case _:
            print("----- Invalid option!! try again!! -----")


while True:
    try:
        main()
    except (ValueError, TypeError) as err:
        print(f"Error Msg: {err}")
        print("Plz try again!!")
        pass
