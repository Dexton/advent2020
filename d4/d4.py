input = open("input", "r")
fields = [
    "byr", # (Birth Year)
    "iyr", # (Issue Year)
    "eyr", # (Expiration Year)
    "hgt", # (Height)
    "hcl", # (Hair Color)
    "ecl", # (Eye Color)
    "pid", # (Passport ID)
    # "cid", # (Country ID) not udes
]

def validate_passport(passport):
    for field in fields:
        if field not in passport["text"]:
            passport["missing"] = field
            return False
    return True

passports = []
next_passport = { "text": "", "isValid": False}
for i, line in enumerate(input):
    if line == '\n':
        next_passport["isValid"] = validate_passport(next_passport)
        passports.append(next_passport)
        next_passport = { "text": "", "isValid": False}
    else:
        next_passport["text"] += line

valid_passport_count = 0
for passport in passports:
    if passport["isValid"]:
        valid_passport_count += 1
print(f"{valid_passport_count} valid passports of {len(passports)}")