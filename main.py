import json

print("Welcome to Review Stream")

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []


def save_task():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def add_a_task():

    add_task = True
    while add_task:
        course = input("Course: ")
        task = input("Task: " )
        due_date = input("Due Date: ")

        task_data = {
            "Course": course,
            "Task": task,
            "Due Date": due_date,
            "Completed": False
        }

        tasks.append(task_data)
        keep_adding = input("Would you like to add another task? (yes/no): ").lower()
        if keep_adding != "yes":
            add_task = False
    save_task()



def view_tasks():

    if not tasks:
        print("No tasks available.")
        return
    
    for number, task_data in enumerate(tasks, start=1):
        status = "X" if task_data["Completed"] else " "
        print(f"{number}). [{status}] {task_data['Course']} - {task_data['Task']} - {task_data['Due Date']}")
    print("\n")


def complete_task():

    if not tasks:
        print("No tasks available to complete.")
        return
    
    try:
        number_to_complete = int(input("Which task number would you like to complete? (Enter the task number): "))
    except ValueError:
        print("Invalid task number. Please enter a valid number.")
        return

    for number, task_data in enumerate(tasks, start=1):
        if number == number_to_complete:
            task_data["Completed"] = True
            print(f"Task number {number_to_complete} has been completed")
            save_task()
            return
        
    print(f"Task number {number_to_complete} not found.")

def delete_task():
    
    if not tasks:
        print("No tasks available to delete.")
        return
    
    try:
        number_to_delete = int(input("Which task number would you like to delete? (Enter the task number): "))
    except ValueError:
        print("Invalid task number. Please enter a valid number.")
        return

    for number, task_data in enumerate(tasks, start=1):
        if number == number_to_delete:
            tasks.remove(task_data)
            print(f"Task number {number_to_delete} has been deleted")
            save_task()
            return
        
    print(f"Task number {number_to_delete} not found.")


def edit_task():

    if not tasks:
        print("No tasks available to edit.")
        return

    try:
        number_to_edit = int(input("Which task number would you like to edit? (Enter the task number): "))
    except ValueError:
        print("Invalid task number. Please enter a valid number.")
        return

    for number, task_data in enumerate(tasks, start=1):
        if number == number_to_edit:
            print(f"Editing task number {number_to_edit}: ")
            new_course = input(f"New Course (current: {task_data['Course']}): ")
            new_task = input(f"New Task (current: {task_data['Task']}): ")
            new_due_date = input(f"New Due Date (current: {task_data['Due Date']}): ")

            task_data["Course"] = new_course if new_course else task_data["Course"]
            task_data["Task"] = new_task if new_task else task_data["Task"]
            task_data["Due Date"] = new_due_date if new_due_date else task_data["Due Date"]

            save_task()
            print(f"Task number {number_to_edit} has been edited.")
            return

    print(f"Task number {number_to_edit} not found.")

def exit_program():

    save_task()

    print("\n" * 2)
    print("...Goodbye...")
    exit()


while True:
    choice = input("Would you like to add a task, view tasks, complete a task, delete a task, edit a task or exit? (add/view/complete/delete/edit/exit): ").lower()

    if choice == "add":
        add_a_task()
    elif choice == "view":
        view_tasks()
    elif choice == "complete":
        complete_task()
    elif choice == "delete":
        delete_task()
    elif choice == "edit":
        edit_task()
    elif choice == "exit":
        exit_program()
    else:
        print("Invalid choice. Please try again.")


