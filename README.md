# Dconf Json

Convert linux gnome config to json and back  
To get the gnome .conf file use:

```bash
dconf dump / > FILENAME.conf
```

Example usage to convert conf and store as json file and take json and store as conf file

```python
import dconfjson

dconfjson.json_writer("FILENAME.conf", dest="FILENAME.json")
dconfjson.dconf_writer("FILENAME.json", dest="FILENAME_2.conf")
```

To load new dconf parameters into gnome use (bash):

```bash
dconf load / < FILENAME_2.conf
```

To get the gnome config out as a python dict use:

```python
import dconfjson

with open(dconf_path, "rb") as fin:
  dconf = fin.read().decode("utf-8")
config_dict = dconfjson.dconf_json(dconf)
```

## Without using files
To get the dconf out as dict without using files:

```python
import dconfjson
import subprocess

def dconf_get():
  spath = "/org/gnome/terminal/legacy/profiles:/"
  cmd = "dconf dump %s /" % spath
  tmp = subprocess.Popen( cmd, shell=True, stdout=subprocess.PIPE )
  (out, err) = tmp.communicate()
  return out
  
s_out = dconf_get().decode("utf-8")
config_dict = dconfjson.dconf_json(s_out)
```
