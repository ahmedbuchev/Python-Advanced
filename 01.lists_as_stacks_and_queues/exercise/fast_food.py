from collections import deque

food_quantity = int(input())
orders_deq = deque([int(el) for el in input().split()])

print(max(orders_deq))

while orders_deq:
    current_order = orders_deq[0]
    if food_quantity < current_order:
        break
    food_quantity -= current_order
    orders_deq.popleft()

if orders_deq:
    print(f'Orders left: {" ".join(str(el) for el in orders_deq)}')
else:
    print("Orders complete")
