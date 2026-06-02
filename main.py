print("Smart Scheduler")

def show_workers(workers):
    for worker in workers:
        print(worker)


def assign_shift(workers,shifts):
    for i in range(len(workers)):
        shift = i % len(shifts)
        print(f"{workers[i]}->{shifts[shift]}")

# assign_shift(workers,shifts)

workers = []
shifts = []

while(True):
    worker_name = input("请输入员工姓名：")
    if(worker_name=="0"):
        print("员工姓名输入完毕!!!")
        break
    workers.append(worker_name)

while(True):
    shift_time = input("请输入轮班时间：")
    if(shift_time=="0"):
        print("轮班时间输入完毕!!!")
        break
    shifts.append(shift_time)

assign_shift(workers,shifts)

