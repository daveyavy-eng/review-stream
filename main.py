import json

print("Welcome to Review Stream")


try:
    with open("tasks.json", "r") as file:
            tasks = json.load(file)
except FileNotFoundError:
    tasks = []


def add_a_task():
    add_task = True
    while add_task:
        course = input("Course: ")
        task = input("Task: " )
        due_date = input("Due Date: ")

        work = {
            "Course": course,
            "Task": task,
            "Due Date": due_date,
            "Completed": False
        }
        tasks.append(work)
        keep_adding = input("Would you like to add another task? (yes/no): ").lower()
        if keep_adding != "yes":
            add_task = False
    with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)        

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        status = "X" if task["Completed"] else " "
        print(f"[{status}] {task['Course']} - {task['Task']} - {task['Due Date']}")
    print("\n")


def complete_task():
    if not tasks:
        print("No tasks available to complete.")
        return
    course_to_complete = input("Which course would you like to complete? (Enter the course name): ")
    task_to_complete = input("Which task would you like to complete? (Enter the task name): ")
    for work in tasks:
        if work["Course"] == course_to_complete and work["Task"] == task_to_complete:
            work["Completed"] = True
            print(f"Course {course_to_complete} {task_to_complete} has been completed")
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
            return
    print(f"Course {course_to_complete} or task {task_to_complete} not found.")
    

def exit_program():
    with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    print("\n" * 2)
    print("...Goodbye...")
    exit()


while True:
    choice = input("Would you like to add a task, view tasks, complete a task, or exit? (add/view/complete/exit): ").lower()

    if choice == "add":
        add_a_task()
    elif choice == "view":
        view_tasks()
    elif choice == "complete":
        complete_task()
    elif choice == "exit":
        exit_program()
    else:
        print("Invalid choice. Please try again.")


