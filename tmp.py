import json

list_id = open("schematic/id_list.txt", "r").readlines()
print(list_id)
json_ready = {}

for ii in list_id:
    id = ii.split(" # ")[0]
    name = (ii.split("(")[-1]).replace(")", "").replace("\n", "")
    json_ready[id] = name

json.dump(json_ready, open("schematic/id_list.json", "w", encoding='utf-8'), ensure_ascii=False, indent=4)
