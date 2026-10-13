import os
import shutil
from pathlib import Path

game = [str(file) for file in Path('game').rglob('*') if file.is_file()]
src = [str(file) for file in Path('src').rglob('*') if file.is_file()]

## GAME
for thin in game:
    doRemove = False

    if thin.endswith(".pdb"):
        doRemove = True

    if thin.find("cfg") > 0:
        doRemove = True


    if thin == "game\\steam_appid.txt":
        doRemove = True
        

    if doRemove:
        os.remove(thin)

## SRC
for thin in src:
    doRemove = False

    # Valve
    if thin.endswith(".vpc.vpc_cache"):
        doRemove = True

    if thin.find("\\_vpc_\\") > 0:
        # shutil.rmtree(thin)
        doRemove = True
    if thin.find("generated_proto_tf") > 0:
        doRemove = True


    # VS
    if thin.endswith(".vcxproj"):
        doRemove = True
    if thin.endswith(".vcxproj.filters"):
        doRemove = True
    if thin.endswith(".vcxproj.vpc_crc"):
        doRemove = True
    if thin.endswith(".vcxproj.user"):
        doRemove = True

    # Builds
    # if thin.find("Debug_") >= 0:
    #     doRemove = True
    # if thin.find("Release_") >= 0:
    #     doRemove = True
    if thin.find("Release") >= 0:
        doRemove = True
    if thin.find("Debug") >= 0:
        doRemove = True


    ## Final
    if thin.endswith(".sln"):
        doRemove = True

    if doRemove:
        if thin.find("NextBot") > 0: continue
        elif thin.find("thirdparty") > 0: continue
        # elif thin.find("materialsystem") > 0: continue
        elif thin.endswith(".inc") > 0: continue
        elif thin.endswith(".cpp") > 0: continue
        elif thin.endswith(".fxc") > 0: continue
        
        print(thin)
        os.remove(thin)

dirs = [
    "src\\game\\server\\Debug_tf",
    "src\\game\\server\\Release_tf"
]

shutil.rmtree("src\\game\\server\\Release_tf")