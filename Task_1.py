import tkinter as tk
from tkinter import messagebox

# ==============================
# Shared Data
# ==============================
tasks = []

# ==============================
# Command-Line Version
# ==============================
def show_tasks():
    if not tasks:
        print("\nNo tasks available.\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task['done'] else "✗"
            print(f"{i}. {task['task']} [{status}]")
    print()

def add_task_cli():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})
    print("Task added successfully!\n")

def mark_done_cli():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark as done: "))
        tasks[task_no - 1]["done"] = True
        print("Task marked as done!\n")
    except:
        print("Invalid task number!\n")

def delete_task_cli():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        tasks.pop(task_no - 1)
        print("Task deleted!\n")
    except:
        print("Invalid task number!\n")

def run_cli():
    while True:
        print("=== TO-DO LIST MENU (CLI) ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task_cli()
        elif choice == '3':
            mark_done_cli()
        elif choice == '4':
            delete_task_cli()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# ==============================
# GUI Version
# ==============================
def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task['done'] else "✗"
        listbox.insert(tk.END, f"{i}. {task['task']} [{status}]")

def add_task_gui():
    task = entry.get()
    if task != "":
        tasks.append({"task": task, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def mark_done_gui():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def delete_task_gui():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task first!")

def run_gui():
    global root, listbox, entry
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("400x400")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    listbox = tk.Listbox(frame, width=40, height=10)
    listbox.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)

    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    add_button = tk.Button(root, text="Add Task", width=15, command=add_task_gui)
    add_button.pack(pady=2)

    done_button = tk.Button(root, text="Mark as Done", width=15, command=mark_done_gui)
    done_button.pack(pady=2)

    delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task_gui)
    delete_button.pack(pady=2)

    root.mainloop()

# ==============================
# Main Menu
# ==============================
if __name__ == "__main__":
    print("Choose To-Do List Mode:")
    print("1. Command-Line (CLI)")
    print("2. Graphical (GUI)")

    choice = input("Enter choice (1/2): ")
    if choice == '1':
        run_cli()
    elif choice == '2':
        run_gui()
    else:
        print("Invalid choice! Exiting...")
