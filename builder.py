import json
import shutil
import os

databr = json.load(open("behavior_pack\manifest.json", "r", encoding='utf-8'))
datarr = json.load(open("resource_pack\manifest.json", "r", encoding='utf-8'))

changenum = input("Какую цифру версии повысить[1.2.3]> ")

info_ver = databr["header"]["version"]

if changenum == "3":
    num = info_ver[2] + 1
    info_ver[2] = num
elif changenum == "2":
    num = info_ver[1] + 1
    info_ver[1] = num
    info_ver[2] = 0
elif changenum == "1":
    num = info_ver[0] + 1
    info_ver[0] = num
    info_ver[1] = 0
    info_ver[2] = 0
else:
    print("Нет изменений в версии")

databr["header"]["version"] = info_ver
databr["modules"][0]["version"] = info_ver
databr["dependencies"][0]["version"] = info_ver

datarr["header"]["version"] = info_ver
datarr["modules"][0]["version"] = info_ver
datarr["dependencies"][0]["version"] = info_ver

json.dump(databr, open("behavior_pack\manifest.json", "w", encoding='utf-8'), ensure_ascii=False, indent=4)
json.dump(datarr, open("resource_pack\manifest.json", "w", encoding='utf-8'), ensure_ascii=False, indent=4)

zip_name_behavior = 'MWAlkoB'
directory_name_behavior = 'behavior_pack'
shutil.make_archive(zip_name_behavior, 'zip', directory_name_behavior)
shutil.move("MWAlkoB.zip", "IMoOB.mcpack")
zip_name_resource = 'MWAlkoR'
directory_name_resource = 'resource_pack'
shutil.make_archive(zip_name_resource, 'zip', directory_name_resource)
shutil.move("MWAlkoR.zip", "IMoOR.mcpack")

opeo_file_q = input("""Открыть файлы в Minecraft["+" для открытия]? >""")
if opeo_file_q == "+":
    os.startfile("IMoOB.mcpack")
    os.startfile("IMoOR.mcpack")