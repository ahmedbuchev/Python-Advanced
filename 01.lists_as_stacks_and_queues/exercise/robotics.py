from collections import deque


def convert_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_seconds_to_str(seconds):
    seconds %= 24 * 60 * 60
    hh = seconds // 3600
    seconds %= 3600
    mm = seconds // 60
    seconds %= 60
    return f"{hh:02d}:{mm:02d}:{seconds:02d}"


robots_data = input().split(";")
process_time_by_robot = {}
busy_time_by_robot = {}

for robot_data in robots_data:
    name, process_time = robot_data.split("-")
    process_time_by_robot[name] = int(process_time)
    busy_time_by_robot[name] = -1

time = convert_str_to_seconds(input())

items = deque()
command = input()
while not command == "End":
    items.append(command)
    command = input()

while items:
    time += 1
    item = items.popleft()

    for name, busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            busy_time_by_robot[name] = time + process_time_by_robot[name]
            print(f"{name} - {item} [{convert_seconds_to_str(time)}]")
            break
    else:
        items.append(item)
