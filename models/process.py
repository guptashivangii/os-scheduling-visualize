class Process:
    def __init__(self,pid,arrival_time,burst_time,priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.remaining_time = burst_time

    def __str__(self):

        return (
            f"{self.pid} | "
            f"AT: {self.arrival_time} | "
            f"BT: {self.burst_time} | "
            f"WT: {self.waiting_time} | "
            f"TAT: {self.turnaround_time}"
        )
print(Process)
