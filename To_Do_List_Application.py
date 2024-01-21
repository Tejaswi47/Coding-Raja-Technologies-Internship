# creating a python programming for the user to create a To_Do_List_Application.
# The To_Do_List_Application allows user to add, remove and mark tasks as completed
# Storing the taks and output in a json file 
# Giving a priority to the task is important. So, Creating a program where user chooses the priority like High, Medium and low

# importing the appropiate modules or libraries

import json
import os
from datetime import datetime

# writing a function to load tasks from a file
def load_tasks():
    try:
        with open('user_tasks.json', 'r') as file:
            return json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading tasks: {e}")
        return []
    
# Writing a function to save the tasks the user entered
def saving_tasks(tasks):
    with open('user_tasks.json', 'w') as file:
        json.dump(tasks, file, indent= 3)
        
# Writing a function to add the tasks the user entered
def adding_the_task(tasks, description, priority, due_date):
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    saving_tasks(tasks)
    print(f"Task added: {description}")
    
# Writing a function to remove the tasks the user wanted
def removing_the_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    removed_task = tasks.pop(index)
    saving_tasks(tasks)
    print(f"Task removed: {removed_task['description']}")

# Writing a function to mark the tasks that user completed
def completed_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    tasks[index]['completed'] = True
    saving_tasks(tasks)
    print(f"Task marked as completed: {tasks[index]['description']}")
    

# Writing a function to  the tasks that user completed
def displaying_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i + 1}. {task['description']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")
            
# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            adding_the_task(tasks, description, priority, due_date)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            removing_the_task(tasks, index)
        elif choice == '3':
            index = int(input("Enter the task number to mark as completed: ")) - 1
            completed_task(tasks, index)
        elif choice == '4':
            displaying_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()