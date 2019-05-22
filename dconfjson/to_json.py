import json
import string
import subprocess

def nesting(data, keys):
    """builds the dict framework
    All fields are left blank
    """
    X = keys
    d = data

    for path in X:
        current_level = d
        for i,part in enumerate(path):
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]
    return d

def nested_set(dic, keys, values):
    """uses the empty framework dict
    sets the values given the dict and keys
    """
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    for li in values:
        dic[keys[-1]][li[0]] = li[1].rstrip() #remove trailing whitespace

def dconf_json(dconf_path):
    """read *.conf file (exported by "dconf dump / > gnome.conf") and export as json.
    Deploys a small hack by using whitespace at end of leafnode keys i.e. "media-keys " in stead of "media-keys"
    This is important or else some conf values will get deleted because of how gnome conf structure its data is not 100% compatible with a hashtable.
    Concrete example: custom-keybindings keyword appear twice in the gnome.conf file.
    """
    with open(dconf_path, "rb") as fin:
        data = dict()
        L, D, C = ([] for i in range(3))
        for line in fin:
            sline = line.decode("utf-8").replace('\n', ' ')
            if sline.startswith("["):
                structure = [a.translate(str.maketrans("", "", "[]\n")) for a in sline.split("/")]
                L.append(structure)
                C.append(D)
                D = []
            elif not sline.isspace():
                D.append(tuple(a.translate(str.maketrans("", "", "\n")) for a in sline.split("=")))
        C.pop(0) # remove first empty element
        C.append(D) # add last element

        nesting(data, L)

        for i, li in enumerate(L):
            nested_set(data, li, C[i])
    return data

def json_writer(dconf_path, dest="output.json"):
    data = dconf_json(dconf_path)
    # save conf as json
    with open(dest, "w", encoding="utf-8") as fout:
        json.dump(data, fout, indent=4)
