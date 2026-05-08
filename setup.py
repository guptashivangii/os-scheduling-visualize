import os

folders = [
    "algorithms",
    "models",
    "gui",
    "utils"
]

files = [
    "main.py",
    "README.md",
    "algorithms/fcfs.py",
    "algorithms/sjf.py",
    "algorithms/round_robin.py",
    "models/process.py",
    "gui/interface.py",
    "utils/gantt_chart.py"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    open(file, "a").close()

print("Project structure created successfully!")
