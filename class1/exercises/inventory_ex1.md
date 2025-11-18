1a. Create an "INI" style inventory file. This file should have an "all:vars" section containing variables for the following:

```
# Replace 'your_user' with your lab username
ansible_python_interpreter=/home/your_user/VENV/py3_venv/bin/python
ansible_user=admin
ansible_password=invalid
```

Additionally, add the following three groups to the inventory file (currently, there are no hosts in these groups):

```
local
gaia
checkpoint
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
            "checkpoint"
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
  |  |--lab_fw_gaia
  |--@checkpoint:
  |  |--lab_fw
```

1c. Modify your inventory file to set the "ansible_network_os" for the gaia and checkpoint groups to:

```bash
ansible_network_os=check_point.gaia.checkpoint
ansible_network_os=check_point.mgmt.checkpoint
```

Additionally, set the "ansible_host" for each of these hosts to the FQDN of the device:

```bash
ansible_host=
 (i.e. cisco1.lasthop.io, arista1.lasthop.io, etc.). Use:


 26 ansible_connection=httpapi
 27 ansible_httpapi_use_ssl=True
 28 ansible_httpapi_validate_certs=False
 29 ansible_user=admin

$ ansible-inventory --list -i ./inventory.ini 
From this output, inspect the inventory and validate that the network_os has been set appropriately. Additionally, add "localhost" to be a member of the "local" group (you will need to set "ansible_connection=local" for the localhost entry).
