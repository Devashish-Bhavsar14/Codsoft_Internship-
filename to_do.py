# To-Do List Manager

todo_list = []

def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. update task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"'{task}' has been added to the list.")

def update_task():
    task = input("Enter the task to update: ")
    
    if task in todo_list:
        new_task=input("enter the task to update")
        index = todo_list.index(task)
        todo_list[index]=new_task
        print(f"'{task}' has been update from the list.")
    else:
        print(f"'{task}' is not in the list.")

def view_tasks():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()