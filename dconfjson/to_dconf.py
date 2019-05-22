import json

def dict_path(my_dict, path=None):
    if path is None:
        path = []
    for k,v in my_dict.items():
        newpath = path + [k]
        if isinstance(v, dict):
            for u in dict_path(v, newpath):
                yield u
        else:
            yield newpath, v

def json_dconf(data):
    conf = ""
    paths = list(dict_path(data))
    current_title = None
    for path in paths:
        title = path[0][:-1]
        if current_title != title:
            # add the title
            conf += "\n[%s]\n" % "/".join(title).strip()
            current_title = title
        #add the values under the title
        conf += "%s=%s\n" % (path[0][-1], path[1])
    if conf[0] == "\n": # remove first newline
        conf = conf[1:]
    return conf 

def conf_writer(json_path, dest="output.conf"):
    """opens json file at path, converts to conf and writes to file at dest
    """
    with open(json_path) as fin:
        data = json.load(fin)
    conf = json_dconf(data)

    # write to file
    with open(dest, "w") as fout:
        fout.write(conf)
