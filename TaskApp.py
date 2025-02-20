import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")
        
        # Creating a list to store tasks
        self.tasks = []
        
        # Creating GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Task Entry
        self.task_entry = tk.Entry(self.root, font=("Arial", 12), width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        # Add Task Button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, font=("Arial", 12), width=40, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # Delete Task Button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)
        
        # Clear All Button
        self.clear_button = tk.Button(self.root, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=10, pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")
    
    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()



    #Now running the code. Hope it goes well....