char_to_bytes = {
    'F': '0', 
    'B': '1',
    'R': '1',
    'L': '0',
}
def calculate_seat_id(row, column):
    return (row*8) + column

def parse_position(pos):
    return (int_from_byte_string(pos[:7]), int_from_byte_string(pos[7:]))

def int_from_byte_string(s):
    return int(s, 2)

def calculate_position(line):
    position = ''
    for char in line:
        if char in char_to_bytes.keys():
            position += char_to_bytes[char]
    return parse_position(position)

input = open("input", "r")
seat_ids = []
for line in input:
    row, column = calculate_position(line)
    seat_ids.append(calculate_seat_id(row, column))
    
    position = ''

test = 'BFFFBBFRRR'
tr, tc = calculate_position(test)
id = calculate_seat_id(tr, tc)
print(f"Test results row {tr} column {tc}\n Valid {id == 567}")

print(f"Maximum seat id is {max(seat_ids)} and minimum {min(seat_ids)}")
for i in range(min(seat_ids), max(seat_ids)):
    if i not in seat_ids:
        print(f"{i} is the missing seat")
