1a. Create an "INI" style inventory file. This file should have an "all:vars" section containing variables for the following:

```
ansible_python_interpreter should be set to "/home/your_user/VENV/py3_venv/bin/python"
ansible_user and ansible_password should be set to 'admin' and the password will be provided
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

2c. Modify your inventory file to set the "ansible_network_os" for the cisco and arista groups to "ios" and "eos" respectively. Additionally, set the "ansible_host" for each of these hosts to the FQDN of the device (i.e. cisco1.lasthop.io, arista1.lasthop.io, etc.). Use:
$ ansible-inventory --list -i ./inventory.ini 
From this output, inspect the inventory and validate that the network_os has been set appropriately. Additionally, add "localhost" to be a member of the "local" group (you will need to set "ansible_connection=local" for the localhost entry).
