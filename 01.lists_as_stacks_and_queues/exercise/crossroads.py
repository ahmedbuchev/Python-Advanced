from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_deque = deque()

command = input()
while not command == "END":
    if command == "green":
        if cars_deque:
            current_car = deque(cars_deque.popleft())
            for _ in range(green_light_duration):
                current_car.popleft()
                if not current_car and cars_deque:
                    current_car = deque(cars_deque.popleft())
                elif not current_car and not cars_deque:
                    break
            if current_car:
                for _ in range(free_window_duration):
                    current_car.popleft()
                    if not current_car:
                        break
    else:
        cars_deque.append(command)
    command = input()
