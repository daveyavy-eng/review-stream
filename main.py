print("Welcome to Review Stream")
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
            "Due Date": due_date
        }
        tasks.append(work)
        keep_adding = input("Would you like to add another task? (yes/no): ").lower()
        if keep_adding != "yes":
            add_task = False


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print("\n")
        print(f"Course: {task['Course']}, Task: {task['Task']}, Due Date: {task['Due Date']}")
        print("\n")

def complete_task():
    if not tasks:
        print("No tasks available to complete.")
        return
    completed_task = input("Which course would you like to complete? (Enter the course name): ")
    for work in tasks:
        if work["Course"] == completed_task:
            tasks.remove(work)
            print(f"Course {completed_task} has been completed and removed.")
            return
    print(f"Course {completed_task} not found.")

def exit_program():
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
