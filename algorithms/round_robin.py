def round_robin_scheduling(processes, quantum):

    processes.sort(key=lambda p: p.arrival_time)

    current_time = 0

    ready_queue = []

    completed = []

    visited = set()

    while len(completed) < len(processes):

        for process in processes:

            if (
                process.arrival_time <= current_time
                and process.pid not in visited
            ):

                ready_queue.append(process)

                visited.add(process.pid)

        if len(ready_queue) == 0:

            current_time += 1

            continue

        current_process = ready_queue.pop(0)

        if current_process.remaining_time <= quantum:

            current_time += current_process.remaining_time

            current_process.remaining_time = 0

            current_process.completion_time = current_time

            current_process.turnaround_time = (
                current_process.completion_time
                - current_process.arrival_time
            )

            current_process.waiting_time = (
                current_process.turnaround_time
                - current_process.burst_time
            )

            completed.append(current_process)

        else:

            current_time += quantum

            current_process.remaining_time -= quantum

            for process in processes:

                if (
                    process.arrival_time <= current_time
                    and process.pid not in visited
                ):

                    ready_queue.append(process)

                    visited.add(process.pid)

            ready_queue.append(current_process)

    return completed