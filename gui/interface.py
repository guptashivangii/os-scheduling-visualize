import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Interface")
root.geometry("900x600")
title_label = tk.Label(
    root,
    text="CPU Scheduling Simulator",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=10)


input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Process ID").grid(row=0, column=0)
pid_entry = tk.Entry(input_frame)
pid_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Arrival Time").grid(row=1, column=0)
arrival_entry = tk.Entry(input_frame)
arrival_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Burst Time").grid(row=2, column=0)
burst_entry = tk.Entry(input_frame)
burst_entry.grid(row=2, column=1)

tk.Label(input_frame, text="Priority").grid(row=3, column=0)
priority_entry = tk.Entry(input_frame)
priority_entry.grid(row=3, column=1)

processes = []

from models.process import Process
def add_process():
    pid = pid_entry.get()
    arrival_time = int(arrival_entry.get())
    burst_time = int(burst_entry.get())
    priority = int(priority_entry.get())
    process = Process(pid, arrival_time, burst_time, priority)
    processes.append(process)
    print(f"{pid} added")
    pid_entry.delete(0, tk.END)
    arrival_entry.delete(0, tk.END)
    burst_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)

add_button = tk.Button(
    root,
    text="Add Process",
    command=add_process
)

add_button.pack(pady=10)
algorithm_var = tk.StringVar()
algorithm_dropdown = ttk.Combobox(
    root,
    textvariable=algorithm_var,
    values=[
        "FCFS",
        "SJF",
        "Round Robin",
        "Priority"
    ]
)
algorithm_dropdown.pack(pady=10)
algorithm_dropdown.current(0)

tk.Label(root, text="Quantum").pack()

quantum_entry = tk.Entry(root)

quantum_entry.pack()

from algorithms.fcfs import fcfs_scheduling
from algorithms.sjf import sjf_scheduling
from algorithms.round_robin import round_robin_scheduling
from algorithms.priority import priority_scheduling

def run_scheduler():

    for item in tree.get_children():

        tree.delete(item)

    selected_algorithm = algorithm_var.get()

    if selected_algorithm == "FCFS":

        result = fcfs_scheduling(processes)

    elif selected_algorithm == "SJF":

        result = sjf_scheduling(processes)

    elif selected_algorithm == "Round Robin":

        quantum = int(quantum_entry.get())

        result = round_robin_scheduling(
            processes,
            quantum
        )

    elif selected_algorithm == "Priority":

        result = priority_scheduling(processes)

    else:

        result = []

    for process in result:

        tree.insert(
            "",
            tk.END,
            values=(
                process.pid,
                process.arrival_time,
                process.burst_time,
                process.waiting_time,
                process.turnaround_time
            )
        )

    total_wt = 0
    total_tat = 0

    for process in result:

        total_wt += process.waiting_time

        total_tat += process.turnaround_time

    avg_wt = total_wt / len(result)

    avg_tat = total_tat / len(result)

    avg_wt_label.config(
        text=f"Average Waiting Time: {avg_wt:.2f}"
    )

    avg_tat_label.config(
        text=f"Average Turnaround Time: {avg_tat:.2f}"
    )

    draw_gantt_chart(result)

def clear_all():

    processes.clear()

    for item in tree.get_children():

        tree.delete(item)

    gantt_canvas.delete("all")

    avg_wt_label.config(
        text="Average Waiting Time: "
    )

    avg_tat_label.config(
        text="Average Turnaround Time: "
    )

    pid_entry.delete(0, tk.END)

    arrival_entry.delete(0, tk.END)

    burst_entry.delete(0, tk.END)

    priority_entry.delete(0, tk.END)

    quantum_entry.delete(0, tk.END)
run_button = tk.Button(
    root,
    text="Run Scheduler",
    command=run_scheduler
)

run_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear All",
    command=clear_all
)

clear_button.pack(pady=10)

columns = (
    "PID",
    "Arrival Time",
    "Burst Time",
    "Waiting Time",
    "Turnaround Time"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=8
)
for col in columns:

    tree.heading(col, text=col)

    tree.column(col, width=120, anchor="center")
tree.pack(pady=10)

avg_wt_label = tk.Label(
    root,
    text="Average Waiting Time: "
)

avg_wt_label.pack()

avg_tat_label = tk.Label(
    root,
    text="Average Turnaround Time: "
)

avg_tat_label.pack()

gantt_canvas = tk.Canvas(
    root,
    width=800,
    height=120,
    bg="white"
)

gantt_canvas.pack(pady=20)
def draw_gantt_chart(processes):

    gantt_canvas.delete("all")

    x = 50
    y = 40

    height = 40
    scale = 40

    current_time = 0

    for process in processes:

        width = process.burst_time * scale

        gantt_canvas.create_rectangle(
            x,
            y,
            x + width,
            y + height,
            fill="lightblue"
        )

        gantt_canvas.create_text(
            x + width / 2,
            y + height / 2,
            text=process.pid
        )

        gantt_canvas.create_text(
            x,
            y + height + 15,
            text=str(current_time)
        )

        current_time += process.burst_time

        gantt_canvas.create_text(
            x + width,
            y + height + 15,
            text=str(current_time)
        )

        x += width
root.mainloop()
