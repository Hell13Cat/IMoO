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

name_item_id = input("ID предмета> ")

type_rec = input("Тип рецепта> ")

if type_rec in ["1"]:
    rec_default = json.load(open("template\\rec"+type_rec+".json", "r", encoding='utf-8'))
    count_res = int(input("Сколько получается> "))
    name_rec_file = name_cat + "_" + name_item_id + ".json"
    rec_default["minecraft:recipe_shaped"]["description"]["identifier"] = name_cat + ":" + name_item_id
    rec_default["minecraft:recipe_shaped"]["result"]["item"] = name_cat + ":" + name_item_id
    rec_default["minecraft:recipe_shaped"]["result"]["count"] = count_res
    json.dump(rec_default, open("behavior_pack\\recipes\\"+name_rec_file, "w", encoding='utf-8', indent=4), ensure_ascii=False)
    print("Рецепт создан!")
else:
    print("Рецепт не будет создан!")

num_frame = int(input("Номер текстуры> ")) - 1

name_item_vis = input("Имя предмета> ")

print("Создание предмета!")