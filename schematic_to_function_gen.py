from nbtschematic import SchematicFile
import json
file_name = input("как называется схема?> ")
sf = SchematicFile.load("schematic/"+file_name+".schematic")
size_locate = sf.blocks.shape

id_list = json.load(open("schematic/id_list.json", "r", encoding='utf-8'))

print("Размер локации:", size_locate[0], "-", size_locate[1], "-", size_locate[2], ". Количество блоков:", size_locate[0]*size_locate[1]*size_locate[2])
text_function = ""

text_addit = ""

count = 0
count_adit = 0

for xx in range(size_locate[0]):
    for yy in range(size_locate[1]):
        for zz in range(size_locate[2]):
            id_block = int(sf.blocks[xx, yy, zz])
            if id_block != 0:
                count += 1
                name_block = id_list[str(id_block)]
                text_add = "setblock ~+" + str(yy) + " ~+" + str(xx) + " ~+" + str(zz) + " " + name_block + "\n"
                text_addit += text_add
                if count == 10000:
                    count_adit += 1
                    open("behavior_pack/functions/fastbuild_"+file_name+"_"+str(count_adit)+".mcfunction", "w").write(text_addit)
                    text_addit = ""
                    count = 0
                    print(count_adit)
count_adit += 1
open("behavior_pack/functions/fastbuild_"+file_name+"_"+str(count_adit)+".mcfunction", "w").write(text_addit)
print(count_adit)