import tkinter as tk
from tkinter import messagebox
import csv

# defining the class using @property dectorator 
class Employee:
    def __init__(self, emp_id, emp_name, salary):
        self._emp_id = emp_id
        self._emp_name = emp_name
        self._salary = salary
    def to_list(self):
        return [self._emp_id, self._emp_name, self._salary]
    
    @staticmethod
    def from_list(data):
        return Employee(data[0], data[1], float(data[2]))
    
    @property
    def emp_id(self):
        return self._emp_id
    
    @property
    def name(self):
        return self._emp_name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._emp_name = value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary 

employee = {}
def add_emp():
    emp_id = entry_id.get()
    name = entry_name.get()
    salary = entry_salary.get()

    if not emp_id or not name or not salary:
        messagebox.showwarning("Input Error", "All fields are reuired")
        return
    try:
        salary = float(salary)
        employee[emp_id] = Employee(emp_id, name, salary)
        messagebox.showinfo("Success", f"Employee {name} added!")
        clear_fields()
    except:
        messagebox.showerror("Error", "Try again")
    
def update_salary():
    emp_id = entry_id.get()
    new_salary = entry_salary.get()
    if emp_id in employee:
        try:
            employee[emp_id].salary = float(new_salary)
            messagebox.showinfo("Updated", "Salary has been updated")
        except:
            messagebox.showerror("Error", "Invalid Salary")

def delete_salary():
    emp_id = entry_id.get()
    if emp_id in employee:
        del employee[emp_id].salary
        messagebox.showinfo("Deleted", "Salary deleted")
    else:
        messagebox.showerror("Not found", "Employee id not found")
        
def view_employee():
    emp_id = entry_id.get()
    if emp_id in employee:
        emp = employee[emp_id]
        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, f"ID : {emp.emp_id}\n")
        text_display.insert(tk.END, f"Name : {emp.name}\n")
        try:
            text_display.insert(tk.END, f"Salary : ${emp.salary}\n")

        except:
            text_display.insert(tk.END, "Salary : Deleted\n")
    else:
        messagebox.showerror("Not Found", "Employee id not found")

def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

def save_csv(filename="employee.csv"):
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Employee ID', 'Name', 'Salary'])
            for emp in employee.values():
                writer.writerow(emp.to_list())
        messagebox.showinfo("Saved", "Employees saved to CSV file")

    except Exception as e:
        messagebox.showerror("Error",str(e))

def load_from_csv(filename='employee.csv'):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) == 3:
                    emp = Employee.from_list(row)
                    employee[emp.emp_id] = emp
            messagebox.showinfo("Loaded", "File has been loaded")
    except FileNotFoundError:
        messagebox.showerror("Not Found", "File not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI layout 
root = tk.Tk()
root.title("Employee Record System")

tk.Label(root, text="Employee ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Salary").grid(row=2, column=0, padx=10, pady=5)
entry_salary = tk.Entry(root)
entry_salary.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Add", command=add_emp).grid(row=3, column=0, padx=10, pady=5)
tk.Button(root, text="Update Salary", command=update_salary).grid(row=3, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Salary", command=delete_salary).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="View", command=view_employee).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="save", command=save_csv).grid(row=7, column=0, pady=5)
tk.Button(root, text="Load csv", command=load_from_csv).grid(row=7, column=1, pady=5)

text_display = tk.Text(root, width=40, height=10)
text_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()