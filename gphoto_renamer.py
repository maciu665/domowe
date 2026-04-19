import sys
import os
from pathlib import Path

orgdir  = Path("/mnt/data/APHOTO/ORG/2026/")

lista = os.listdir(orgdir)
lista.sort()
#sys.exit()
for i in lista:
    # replace all spaces in filename with underscores
    if " " in i or ".." in i or "dsc" in i.lower() or "mov" in i.lower()  or "vid" in i.lower() or "img" in i.lower() or "burst" in i.lower() or "hdr" in i.lower() or "pano" in i.lower():
        newname = i.replace(" ", "_").replace("..", ".").replace("dsc","DSC").replace("mov","MOV").replace("vid","VID").replace("img","IMG").replace("burst","BURST").replace("hdr","HDR").replace("pano","PANO").replace("pint","Pint")
        #print(f"Renaming {i} -> {newname}")
        os.rename(orgdir / i, orgdir / newname)
    if "pinterest" in i or "chrome" in i or "facebo" in i or "messenger" in i or "screenshot" in i or "fb_" in i:
        newname = i.replace("pinterest","Pinterest").replace("chrome","Chrome").replace("faceb","Faceb").replace("messenger","Messenger").replace("screenshot","Screenshot").replace("fb_","FB_")
        #print(f"Renaming {i} -> {newname}")
        os.rename(orgdir / i, orgdir / newname)
    if "google" in i or "drive" in i or "messages" in i or "gallery" in i or "whatsa" in i or "hangouts" in i or "gmail" in i:
        newname = i.replace("google","Google").replace("drive","Drive").replace("messages","Messages").replace("gallery","Gallery").replace("whatsa","WhatsA").replace("hangouts","Hangouts").replace("gmail","Gmail")
        print(f"Renaming {i} -> {newname}")
        os.rename(orgdir / i, orgdir / newname)
    if "allegro" in i or "zalando" in i or "youtube" in i or "maps" in i or "one_ui_home" in i or "samsung_notes" in i or "_camera" in i:
        newname = i.replace("allegro","Allegro").replace("zalando","Zalando").replace("youtube","YouTube").replace("maps","Maps").replace("one_ui_home","One_UI_Home").replace("samsung_notes","Samsung_Notes").replace("_camera","_Camera")
        print(f"Renaming {i} -> {newname}")
        os.rename(orgdir / i, orgdir / newname)
###

lista = os.listdir(orgdir)
lista.sort()

renames = []

for i in lista:
    if i.lower().endswith(".json"):
        #print(i)
        if ".mp4." in i.lower():
            newname = i.lower().split(".mp4.")[0] + ".json"
            renames.append((i, newname))
        if ".jpg." in i.lower():
            newname = i.lower().split(".jpg.")[0] + ".json"
            renames.append((i, newname))
        if ".png." in i.lower():
            newname = i.lower().split(".png.")[0] + ".json"
            renames.append((i, newname))

print("Renames:")
for o, n in renames:
    print(f"{o} -> {n}")
    os.rename(orgdir / o, orgdir / n)
    
# 
lista = os.listdir(orgdir)
lista.sort()

renames = []

unpaired_jsons = []
for i in lista:
    if i.lower().endswith(".json"):
        haspaitr = False
        for j in lista:
            if j.lower().endswith(".json") == False:
                if Path(j).stem == Path(i).stem:
                    haspaitr = True
                    break
        if haspaitr == False:
            unpaired_jsons.append(i)

rename_json2file = []
rename_file2json = []
print("Unpaired JSONs:")
for i in unpaired_jsons:
    print(i)
    for j in lista:
        if j.lower().endswith(".json") == False:
            if Path(i).stem.startswith(Path(j).stem):
                print(f"  Possible pair: {j}")
                rename_json2file.append((i, j))
            if Path(j).stem.startswith(Path(i).stem):
                print(f"  Possible pair: {j}")
                rename_file2json.append((j, i))
print()
for i in rename_json2file:
    print(f"Renaming {i[0]} --> {Path(i[1]).stem}.json")
    os.rename(orgdir / i[0], orgdir / f"{Path(i[1]).stem}.json")
for i in rename_file2json:
    print(f"Renaming {i[1]} -> {Path(i[0]).stem}{Path(i[1]).suffix}")
    os.rename(orgdir / i[1], orgdir / f"{Path(i[0]).stem}{Path(i[1]).suffix}")

lista = os.listdir(orgdir)
lista.sort()
#sys.exit()
for i in lista:
    # replace all spaces in filename with underscores
    if " " in i or ".." in i or "dsc" in i.lower() or "mov" in i.lower()  or "vid" in i.lower() or "img" in i.lower() or "burst" in i.lower() or "hdr" in i.lower():
        newname = i.replace(" ", "_").replace("..", ".").replace("dsc","DSC").replace("mov","MOV").replace("vid","VID").replace("img","IMG").replace("burst","BURST").replace("hdr","HDR")
        #print(f"Renaming {i} -> {newname}")
        os.rename(orgdir / i, orgdir / newname)