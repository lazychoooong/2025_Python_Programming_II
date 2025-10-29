import tkinter as tk
import pickle

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do 리스트")
        
        self.tasks = []
        self.load_tasks()  # 기존 작업 불러오기
        
        self.task_var = tk.StringVar()
        
        self.task_entry = tk.Entry(root, textvariable=self.task_var)
        self.task_entry.pack(pady=10)
        
        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="추가", command=self.add_task)
        self.add_button.pack()
        
        self.complete_button = tk.Button(root, text="완료 표시", command=self.mark_complete)
        self.complete_button.pack()

        self.save_button = tk.Button(root, text="저장", command=self.save_tasks)
        self.save_button.pack()
        
        self.display_tasks()  # 작업 목록 표시
        
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_quit)  # 윈도우 닫을 때 저장
        
    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_var.set("")
            self.display_tasks()
    
    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.display_tasks()
    
    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_name = task["task"]
            if task["completed"]:
                task_name += " (Completed)"
            self.task_listbox.insert(tk.END, task_name)
    
    def save_tasks(self):
        with open("tasks.pkl", "wb") as f:
            pickle.dump(self.tasks, f)
    
    def load_tasks(self):
        try:
            with open("tasks.pkl", "rb") as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            pass
    
    def save_and_quit(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()