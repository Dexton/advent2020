input = open("input", "r")
groups = []
group = {}

for line in input:
    if line == '\n':
        groups.append(group)
        group = {}
    for char in line.strip():
        group[char] = True

count = 0
for group in groups:
    print(len(group))
    count += len(group)
print(count)