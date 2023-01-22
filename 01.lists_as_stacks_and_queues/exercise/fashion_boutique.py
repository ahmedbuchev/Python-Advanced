clothes = [int(el) for el in input().split()]
rack_capacity = int(input())

used_racks = 1
current_rack_capacity = rack_capacity

while clothes:
    current_piece = clothes[-1]
    if current_rack_capacity >= current_piece:
        current_rack_capacity -= current_piece
        clothes.pop()
    else:
        used_racks += 1
        current_rack_capacity = rack_capacity
print(used_racks)
