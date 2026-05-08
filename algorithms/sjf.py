def sjf_scheduling(processes):

    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0

    completed = []

    ready_queue = []

    while len(completed) < len(processes):

        # Add arrived processes
        for process in processes:

            if (
                process.arrival_time <= current_time
                and process not in ready_queue
                and process not in completed
            ):

                ready_queue.append(process)

        # CPU idle case
        if len(ready_queue) == 0:

            current_time += 1
            continue

        # Select shortest burst process
        ready_queue.sort(key=lambda p: p.burst_time)

        current_process = ready_queue.pop(0)

        # Execute process
        current_time += current_process.burst_time

        # Calculate metrics
        current_process.completion_time = current_time

        current_process.turnaround_time = (
            current_process.completion_time
            - current_process.arrival_time
        )

        current_process.waiting_time = (
            current_process.turnaround_time
            - current_process.burst_time
        )

        # Mark completed
        completed.append(current_process)

    return completed