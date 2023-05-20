import json

def readMusicDef():
    with open('./preferences/musicdef.json', 'r') as f:
        data = json.load(f)

    print(data)
    return data