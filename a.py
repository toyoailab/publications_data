import json
import os

target = "domestic"
data = None
with open(target + "_all.json", "r") as f:
    data = json.load(f)

new_data = {}
for line in data:
    year = line["year"]
    print(line["year"])
    try:
        new_data[year].append(line)
    except KeyError:
        new_data.update({year:[]})
        new_data[year].append(line)

try:
    while True:
        l = new_data.popitem()
        with open(target + l[0] + ".json", "w") as f:
            json.dump(l[1], f, ensure_ascii=False, indent=4)
except:
    pass
