tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if tasks:
        print("Tasks:")
        for num, task in enumerate(tasks, start=1):
            print(f"{num}. {task}")
    else:
        print("Theres is No tasks to display")


def complete_task(task_num):
    if 1 <= task_num <= len(tasks):
        completed_task = tasks.pop(task_num - 1)
        print(f"Task '{completed_task}' marked as completed")
    else:
        print("Invalid task")


def about_me():
    about = '''Hi, I am Naveen Singh Rawat I am 18 Years old and pursuing Btech From COER University (Roorkee)
    I have Completed my 10+2 From Jwalapur Inter college Haridwar , i am doing this 4week internship from codsoft '''
    print(about)


while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Finished")
    print("4. About")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_num = int(
            input("Enter the Number of the task to mark as Finished: "))
        complete_task(task_num)
    elif choice == "4":
        about_me()
    elif choice == "5":
        print("Thankyou, Goodbye!")
        break

    else:
        print("Invalid choice")
