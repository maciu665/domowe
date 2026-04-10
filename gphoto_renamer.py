import sys
import os
from pathlib import Path

orgdir  = Path("/mnt/data/APHOTO/ORG/2015/")

lista = os.listdir(orgdir)
lista.sort()

renames = []

for i in lista:
    if i.lower().endswith(".json"):
        #print(i)
        if ".mp4." in i.lower():
            newname = i.split(".mp4.")[0] + ".json"
            renames.append((i, newname))
        if ".jpg." in i.lower():
            newname = i.split(".jpg.")[0] + ".json"
            renames.append((i, newname))
        if ".png." in i.lower():
            newname = i.split(".png.")[0] + ".json"
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
    print(f"Renaming {i[0]} -> {Path(i[1]).stem}.json")
    os.rename(orgdir / i[0], orgdir / f"{Path(i[1]).stem}.json")
for i in rename_file2json:
    print(f"Renaming {i[1]} -> {Path(i[0]).stem}{Path(i[1]).suffix}")
    os.rename(orgdir / i[1], orgdir / f"{Path(i[0]).stem}{Path(i[1]).suffix}")

lista = os.listdir(orgdir)
lista.sort()
#sys.exit()
for i in lista:
    # replace all spaces in filename with underscores
    if " " in i or ".." in i:
        newname = i.replace(" ", "_").replace("..", ".")
        #print(f"Renaming {i} -> {newname}")
        os.rename(orgdir / i, orgdir / newname)