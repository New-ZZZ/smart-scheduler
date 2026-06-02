print("Smart Scheduler")

def show_workers(workers):
    for worker in workers:
        print(worker)

workers = ["Alice","Bob","Tom"]
shifts = ["Day","Night"]

for i in range(len(workers)):
    shift = i % len(shifts)
    print(workers[i],"->",shifts[shift])
