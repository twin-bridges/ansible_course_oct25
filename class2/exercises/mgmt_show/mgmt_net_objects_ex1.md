
Use the cp_mgmt_network_facts module to retrieve Network Object facts (register the
outptu from this module).

Process the registered output from this module and extract the default office address
pool. You can assume this is the first object in the returned list of network objects.

From this office address pool use the set_fact module to extract the "name", "subnet4",
and "subnet-mask" field.

Use the debug module to print out these three variables (name, network/netmask). Your
output should look similar to the following.

```bash
$ ansible-playbook ex_mgmt_net_objects.yml --limit pod1-mgmt

PLAY [Network objects] ********************************************************************

TASK [Retrieve network objects] ***********************************************************
ok: [pod1-mgmt]

TASK [Retrieve default office address pool] ***********************************************
ok: [pod1-mgmt]

TASK [Retreive object details] ************************************************************
ok: [pod1-mgmt]

TASK [Print object info] ******************************************************************
ok: [pod1-mgmt] => {
    "msg": "\"Name: CP_default_Office_Mode_addresses_pool\"\n\"Network: 172.16.10.0/255.255.255.0\"\n"
}

PLAY RECAP ********************************************************************************
pod1-mgmt   : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
