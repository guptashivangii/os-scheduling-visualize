from models.process import Process
from algorithms.priority import priority_scheduling

processes = [
    Process("P1", 0, 5, 2),
    Process("P2", 1, 3, 1),
    Process("P3", 2, 2, 3)
]

scheduled_processes = priority_scheduling(processes)

for process in scheduled_processes:
    print(process)