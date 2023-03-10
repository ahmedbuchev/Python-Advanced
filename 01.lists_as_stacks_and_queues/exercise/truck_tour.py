from collections import deque

n = int(input())

pumps = deque()

for _ in range(n):
    pumps_data = [int(el) for el in input().split()]
    pumps.append(pumps_data)

for attempt in range(n):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        pumps.rotate(-1)
        # pumps.append(pumps.popleft())
    else:
        print(attempt)
        break
