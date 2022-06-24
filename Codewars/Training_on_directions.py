opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

plan = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

direction = []
for d in plan:
    if direction and direction[-1] == opposite[d]:
        print(direction)
        
        direction.pop()
    else:
        direction.append(d)
print(direction)