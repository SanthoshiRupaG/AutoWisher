import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
# Function to save the data to CSV
def save_to_csv():
    data = {
        "PatientGender": entry_gender.get(),
        "PatientAge": entry_age.get(),
        "PatientRegion": entry_address.get(),
        "Doctor consulted ": entry_doctor.get(),
        "Department": entry_department.get(),
        "Case Description": entry_case.get(),
        "Severity": entry_severity.get(),
        "Bill Amount": entry_bill.get(),
        "Insurance":0,
        "Final bill":entry_bill.get()
    }
    df = pd.DataFrame([data])
    df.to_csv('finaldata.csv', mode='a', index=False, header=False)
    messagebox.showinfo("Success", "Data saved to CSV successfully!")


# Function to display the next chart
def show_next_chart():
    global chart_index
    if chart_index < len(charts):
        charts[chart_index]()
        chart_index += 1
    else:
        messagebox.showinfo("Info", "No more charts to display.")

# Example charts
def chart1():
    df = pd.read_csv('finaldata.csv')
    fig, ax = plt.subplots()
    df['PatientAge'].value_counts().plot(ax=ax, kind='bar')
    ax.set_title('Age Distribution')
    display_chart(fig)

def chart2():
    df = pd.read_csv('finaldata.csv')
    fig, ax = plt.subplots()
    df['PatientGender'].value_counts().plot(ax=ax, kind='pie', autopct='%1.1f%%')
    ax.set_title('Gender Distribution')
    display_chart(fig)

def chart3():
    df = pd.read_csv('finaldata.csv')
    fig, ax = plt.subplots()
    df['Age Category'] = pd.cut(df['PatientAge'], bins=[0, 18, 50, 100],labels=['Children', 'Adults', 'Senior Citizens'])
    df['Age Category'].value_counts().plot(ax=ax,kind='pie',startangle=140,colors=['#ff9999', '#66b3ff', '#99ff99'] )
    ax.set_title('Distribution of Patients by Age Category')
    display_chart(fig)

def chart4():
    df = pd.read_csv('finaldata.csv')
    fig, ax = plt.subplots()
    df['Department'].value_counts().reset_index().plot(ax=ax,kind='bar',color='skyblue',xlabel='Department',ylabel='No of patients')
    '''department_counts = df['Department'].value_counts().reset_index()
    department_counts.columns = ['Department', 'Count']

    # Plot the distribution of patients per department using a histogram
    plt.figure(figsize=(12, 8))
    department_counts['Department'].plot(ax=ax, kind='bar', color='skyblue')
   
    ax.set_xlabel('Department')
    ax.set_ylabel('Patients')'''
    ax.set_title('Distribution of Patients by Age Category')
    display_chart(fig)

# Function to display the chart in the Tkinter window
def display_chart(fig):
    for widget in chart_frame.winfo_children():
        widget.destroy()
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# List of charts to display
charts = [chart1, chart2,chart3,chart4]
chart_index = 0

# Creating the main window
root = tk.Tk()
root.title("Analytics Input Form")

# Creating the input fields
tk.Label(root, text="Name").grid(row=0)
tk.Label(root, text="Age").grid(row=1)
tk.Label(root, text="Gender").grid(row=2)
tk.Label(root, text="Address").grid(row=3)
tk.Label(root, text="Case").grid(row=4)
tk.Label(root, text="Department").grid(row=5)
tk.Label(root, text="Doctor Name").grid(row=6)
tk.Label(root, text="Severity").grid(row=7)
tk.Label(root, text="Bill Amount").grid(row=8)

entry_name = tk.Entry(root)
entry_age = tk.Entry(root)
entry_gender = tk.Entry(root)
entry_address = tk.Entry(root)
entry_case = tk.Entry(root)
entry_department = tk.Entry(root)
entry_doctor = tk.Entry(root)
entry_severity = tk.Entry(root)
entry_bill = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_age.grid(row=1, column=1)
entry_gender.grid(row=2, column=1)
entry_address.grid(row=3, column=1)
entry_case.grid(row=4, column=1)
entry_department.grid(row=5, column=1)
entry_doctor.grid(row=6, column=1)
entry_severity.grid(row=7, column=1)
entry_bill.grid(row=8, column=1)

# Creating buttons
tk.Button(root, text="Save to CSV", command=save_to_csv).grid(row=9, column=0)
tk.Button(root, text="Next Chart", command=show_next_chart).grid(row=9, column=1)

# Frame for displaying charts
chart_frame = tk.Frame(root)
chart_frame.grid(row=10, column=0, columnspan=2)

root.mainloop()
