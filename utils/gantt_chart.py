def display_gantt_chart(processes):

    gantt_chart = ""
    timeline = ""

    first_process = processes[0]

    first_start = (
        first_process.completion_time
        - first_process.burst_time
    )

    timeline += str(first_start)

    for process in processes:

        gantt_chart += f"| {process.pid} "

        timeline += " " * 5

        timeline += str(process.completion_time)

    print("\nGantt Chart:\n")

    print(gantt_chart + "|")

    print(timeline)