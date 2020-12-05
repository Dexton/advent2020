from re import match

input = open("input", "r")

def RepresentsInt(s):
    try:
        i = int(s)
        return i
    except:
        return False

def ValidByr(value):
    value = RepresentsInt(value)
    return value and (value >= 1920 and value <= 2002)

def ValidIyr(value):
    value = RepresentsInt(value)
    return value and (value >= 2010 and value <= 2020)

def ValidEyr(value):
    value = RepresentsInt(value)
    return value and (value >= 2020 and value <= 2030)

def ValidHgt(value):
    height = value[:-2]
    height = RepresentsInt(height)
    unit = value[-2:]
    if not height:
        return False
    if unit == 'cm' and height >= 150 and height <= 193:
        return True
    if unit == 'in' and height >= 59 and height <= 76:
        return True
    return False

def ValidHcl(value):
    return match("^#[0-9a-f]{6}$", value) != None

def ValidEcl(value):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for color in colors:
        if value == color:
            return True
    return value in colors

def ValidPid(value):
    return match("^[0-9]{9}$", value) != None

fields_to_validator = {
    "byr": ValidByr, # (Birth Year)
    "iyr": ValidIyr, # (Issue Year)
    "eyr": ValidEyr, # (Expiration Year)
    "hgt": ValidHgt, # (Height)
    "hcl": ValidHcl, # (Hair Color)
    "ecl": ValidEcl, # (Eye Color)
    "pid": ValidPid, # (Passport ID)
    # "cid", # (Country ID) not udes
}

def ValidatePassport(passport):
    field_map = passport["field_map"]
    for field in fields_to_validator.keys():
        if field not in field_map.keys():
            passport["missing"] = field
            return False
        validator = fields_to_validator[field]
        if not validator(field_map[field]):
            passport["invalid"] = f"{field}: {field_map[field]}"
            return False
    return True

def ParsePassPortMaps(text):
    maps = {}
    if ':' not in text:
        return maps
    text_by_spaces_and_lbs = []
    text_by_spaces = text.split(' ')
    for text in text_by_spaces:
        if ':' not in text:
            continue
        text_by_spaces_and_lbs += text.split('\n')
    for text in text_by_spaces_and_lbs:
        if ':' not in text:
            continue
        halfs = text.split(':')
        maps[halfs[0]] = halfs[1]
    return maps

passports = []
next_passport = { "text": "", "isValid": False}
for i, line in enumerate(input):
    if line == '\n':
        next_passport["field_map"] = ParsePassPortMaps(next_passport["text"])
        next_passport["isValid"] = ValidatePassport(next_passport)
        passports.append(next_passport)
        next_passport = { "text": "", "isValid": False}
    else:
        next_passport["text"] += line

valid_passport_count = 0
for passport in passports:
    if passport["isValid"]:
        valid_passport_count += 1
print(f"{valid_passport_count} valid passports of {len(passports)}")