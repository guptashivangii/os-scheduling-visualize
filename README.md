# CPU Scheduling Simulator

A GUI-based Operating System scheduling simulator developed using Python and Tkinter.

This project demonstrates the implementation and visualization of major CPU scheduling algorithms used in Operating Systems.

---

## Features

* FCFS (First Come First Serve) Scheduling
* SJF (Shortest Job First) Scheduling
* Round Robin Scheduling
* Priority Scheduling
* Gantt Chart Visualization
* Average Waiting Time Calculation
* Average Turnaround Time Calculation
* Interactive GUI using Tkinter
* Process Management and Reset Functionality
* Flask-based REST API support
* FCFS API endpoint with JSON request handling
* Postman API testing


---

## Technologies Used

* Python
* Tkinter
---

## Project Structure

```bash
Process scheduler/
│
├── algorithms/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── round_robin.py
│   └── priority.py
│
├── gui/
│   └── interface.py
│
├── models/
│   └── process.py
│
├── README.md
├── main.py
└── setup.py
```

---

## Implemented Scheduling Algorithms

### 1. FCFS (First Come First Serve)

Processes are executed in the order of arrival.

### 2. SJF (Shortest Job First)

Processes with smaller burst times are executed first.

### 3. Round Robin

Processes are executed using a fixed time quantum.

### 4. Priority Scheduling

Processes with higher priority are executed first.

---

## GUI Features

* Add Processes Dynamically
* Select Scheduling Algorithm
* Enter Quantum for Round Robin
* View Scheduling Results in Table Format
* Visualize Execution using Gantt Chart
* Clear All Functionality

---

---

## REST API Support

The project includes a Flask-based REST API implementation for CPU scheduling algorithms.

### Implemented Endpoint

| Endpoint | Method | Description         |
| -------- | ------ | ------------------- |
| `/fcfs`  | POST   | Run FCFS Scheduling |

---

## Example JSON Request

```json
{
    "processes": [
        {
            "pid": "P1",
            "arrival_time": 0,
            "burst_time": 5,
            "priority": 1
        },
        {
            "pid": "P2",
            "arrival_time": 1,
            "burst_time": 3,
            "priority": 2
        }
    ]
}
```

---

## API Technologies Used

* Flask
* REST APIs
* JSON
* Postman

---

## Running the API Server

```bash
python -m api.app
```

The API runs locally on:

```text
http://127.0.0.1:5000
```

## Performance Metrics

The simulator calculates:

* Waiting Time (WT)
* Turnaround Time (TAT)
* Average WT
* Average TAT

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/guptashivangii/os-scheduling-visualize.git
```

### Navigate to Project Folder

```bash
cd os-scheduling-visualize
```

### Run GUI

```bash
python -m gui.interface
```

---

## Future Improvements

* Animated Gantt Chart
* CPU Utilization Graphs
* Dark Mode GUI
* Multi-Core Scheduling Simulation
* Export Scheduling Results

---

## Author

Shivangi Gupta
