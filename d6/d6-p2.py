input = open("input", "r")
groups = []
group = set()
first_in_group = True

for line in input:
    person = set()

    if line == '\n':
        groups.append(group)
        group = {}
        first_in_group = True
        continue

    for char in line.strip():
        person.add(char)
    if first_in_group:
        group = person
        first_in_group = False
    else:
        # Set the group as all the yes answers from this person that match the
        # yes answers from the previous persons in the group
        group = group.intersection(person)


count = 0
for i, group in enumerate(groups):
    print(f"{i+1}: {len(group)} {group}")
    count += len(group)
print(count)