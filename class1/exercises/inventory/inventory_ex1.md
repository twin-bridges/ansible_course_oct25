1a. Create an "INI" style inventory file. This file should have an "all:vars" section containing variables for the following:

```
# Replace 'studentX' with your lab username
ansible_python_interpreter=/home/studentX/VENV/py3_venv/bin/python
ansible_user=admin
ansible_password=invalid
```

Additionally, add the following three groups to the inventory file (currently, there are no hosts in these groups):

```
local
gaia
mgmt
```

Use:

```bash
$ ansible-inventory --list -i ./inventory_ex1a.ini
```

To validate and inspect your inventory file, your output should look similar to the following:

```json
{
    "_meta": {
        "hostvars": {}
    },
    "all": {
        "children": [
            "ungrouped",
            "local",
            "gaia",
            "mgmt"
        ]
    }
}
```

1b. Add one host to the local, gaia, and checkpoint groups and re-inspect the inventory using:

```bash
$ ansible-inventory --list -i ./inventory_ex1b.ini
```

Additionally, use the --graph option. This option provides a more compressed view of your inventory. Your --graph output should look similar to the following:

```bash
$ ansible-inventory --graph -i ./inventory_ex1b.ini 
@all:
  |--@ungrouped:
  |--@local:
  |  |--localhost
  |--@gaia:
  |  |--lab_gaia
  |--@mgmt:
  |  |--lab_mgmt
```

1c. Modify your inventory file to set the "ansible_network_os" for the gaia and mgmt groups to:

```bash
ansible_network_os=check_point.gaia.checkpoint
ansible_network_os=check_point.mgmt.checkpoint
```

This should be in ":vars" section for the given group.

Execute the "ansible-inventory" command using the "lab_gaia" host, your output should look similar to the following:

```bash
$ ansible-inventory --host lab_gaia -i ./inventory_ex1c.ini 
```

```json
{
    "ansible_network_os": "check_point.gaia.checkpoint",
    "ansible_password": "invalid",
    "ansible_python_interpreter": "/home/studentX/VENV/py3_venv/bin/python",
    "ansible_user": "admin"
}
```
