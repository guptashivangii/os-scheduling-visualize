from flask import Flask, request, jsonify

from models.process import Process
from algorithms.fcfs import fcfs_scheduling

app = Flask(__name__)

@app.route("/")
def home():

    return "CPU Scheduling API Running"


@app.route("/fcfs", methods=["POST"])
def fcfs_api():

    data = request.get_json()

    processes_data = data["processes"]

    processes = []

    for p in processes_data:

        process = Process(
            p["pid"],
            p["arrival_time"],
            p["burst_time"],
            p["priority"]
        )

        processes.append(process)

    result = fcfs_scheduling(processes)

    output = []

    for process in result:

        output.append({
            "pid": process.pid,
            "arrival_time": process.arrival_time,
            "burst_time": process.burst_time,
            "waiting_time": process.waiting_time,
            "turnaround_time": process.turnaround_time
        })

    return jsonify(output)


if __name__ == "__main__":

    app.run(debug=True)