import json

bp_root = "/behavior_pack"
item_default = json.load(open("template\item.json", "r", encoding='utf-8'))
texture_list = json.load(open("resource_pack\\textures\item_texture.json", "r", encoding='utf-8'))

texture_keys = list((texture_list["texture_data"]).keys())
count = 0
keys_succ = []
for ii in texture_keys:
    print(count, "-", ii)
    keys_succ.append(str(count))
    count += 1
name_cat_t = input("Имя категории предмета> ")
if name_cat_t in keys_succ:
    name_cat = texture_keys[int(name_cat_t)]
else:
    name_cat = name_cat_t

for ii in texture_list["texture_data"][name_cat]["textures"]:
    print("-", ii)

name_item_id = input("ID предмета> ")
type_rec = input("Тип рецепта> ")
name_file = name_cat + "_" + name_item_id + ".json"

if type_rec in ["1"]:
    rec_default = json.load(open("template\\rec"+type_rec+".json", "r", encoding='utf-8'))
    count_res = int(input("Сколько получается> "))
    rec_default["minecraft:recipe_shaped"]["description"]["identifier"] = name_cat + ":" + name_item_id
    rec_default["minecraft:recipe_shaped"]["result"]["item"] = name_cat + ":" + name_item_id
    rec_default["minecraft:recipe_shaped"]["result"]["count"] = count_res
    json.dump(rec_default, open("behavior_pack\\recipes\\"+name_file, "w", encoding='utf-8'), ensure_ascii=False, indent=4)
    print("Рецепт создан!")
else:
    print("Рецепт не будет создан!")

count = 1
for ii in texture_list["texture_data"][name_cat]["textures"]:
    print(count, "-", ii)
    count += 1
num_frame = int(input("Номер текстуры> ")) - 1

name_item_vis = input("Видимое имя предмета> ")
name_cati_d = {"0":"none", "1":"construction", "2":"equipment", "3":"items", "4":"nature"}
print("0 - None\n1 - Construction\n2 - Equipment\n3 - Items\n4 - Nature")
name_cati_t = input("Имя категории предмета в инвентаре> ")
item_default["minecraft:item"]["description"]["category"] = name_cati_d[name_cati_t]
item_default["minecraft:item"]["description"]["identifier"] = name_cat + ":" + name_item_id
item_default["minecraft:item"]["components"]["minecraft:icon"]["texture"] = name_cat
item_default["minecraft:item"]["components"]["minecraft:icon"]["frame"] = num_frame
item_default["minecraft:item"]["components"]["minecraft:display_name"]["value"] = name_item_vis
json.dump(item_default, open("behavior_pack\\items\\"+name_file, "w", encoding='utf-8'), ensure_ascii=False, indent=4)
print("Предмет создан!")