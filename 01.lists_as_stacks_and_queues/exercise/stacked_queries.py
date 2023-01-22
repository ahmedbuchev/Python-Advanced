nums_stack = []
reversed_stack = []
n = int(input())

for _ in range(n):
    command_split = input().split()
    cmd = command_split[0]
    if cmd == "1":
        nums_stack.append(int(command_split[1]))
    elif cmd == "2" and nums_stack:
        nums_stack.pop()
    elif cmd == "3" and nums_stack:
        print(max(nums_stack))
    elif cmd == "4" and nums_stack:
        print(min(nums_stack))

while nums_stack:
    reversed_stack.append(str(nums_stack.pop()))

print(", ".join(reversed_stack))
