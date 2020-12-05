input = open("input", "r")
rows = []
right = 3
down = 1

for line in input:
    row = []
    for char in line:
        if char == '#':
            row.append(True)
        elif char == '.':
            row.append(False)
    rows.append(row)

def ride(right, down):
    trees = 0
    for i, row in enumerate(rows):
        if i == 0 or i % down > 0:
            continue
        x_position = right*(i/down) % len(row)
        if row[int(x_position)]:
            trees += 1
    return trees

r1d1 = ride(1, 1)
r3d1 = ride(3, 1)
r5d1 = ride(5, 1)
r7d1 = ride(7, 1)
r1d2 = ride(1, 2)

print(f"R1D1: {r1d1}, R3D1: {r3d1}, R5D1: {r5d1}, R7D1: {r7d1}, R1D2: {r1d2}")
print(f"{r1d1*r3d1*r5d1*r7d1*r1d2}")