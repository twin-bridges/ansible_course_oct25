2a. Create a new directory that includes a Playbook and a "group_vars" directory. 

The group_vars directory should contain a "gaia" subdirectory. Inside this "group_vars/gaia" subdirectory, create a file named "dns.yml". Inside this "dns.yml" file create a variable for "dns1" and assign it a value of "172.31.0.2". 

Create a playbook that runs against the "gaia" group. Inside this playbook create a task using the "debug" module to print a message to stdout containing this "dns1" variable. The message should look similar to the following:

```bash
$ ansible-playbook exercise2a.yml 

PLAY [Exercise 2a] **********************************************************************

TASK [Print 'dns1' for gaia hosts] ******************************************************
[WARNING]: No inventory was parsed, only implicit localhost is available
ok: [pod2-gaia] => {
    "msg": "Primary DNS for host pod2-gaia is 172.31.0.2"
}
ok: [pod1-gaia] => {
    "msg": "Primary DNS for host pod1-gaia is 172.31.0.2"
}
ok: [pod4-gaia] => {
    "msg": "Primary DNS for host pod4-gaia is 172.31.0.2"
}
ok: [pod3-gaia] => {
    "msg": "Primary DNS for host pod3-gaia is 172.31.0.2"
}
ok: [pod5-gaia] => {
    "msg": "Primary DNS for host pod5-gaia is 172.31.0.2"
}

PLAY RECAP ******************************************************************************
pod1-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod2-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod3-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod4-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod5-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

2b. Create a "host_vars" directory, and a subdirectory named "pod5-gaia" within it. Inside this, "host_vars/pod5-gaia" directore, create a file named "dns.yml". 

Inside this file, create a variable named "dns1", but this time using a value of "8.8.8.8". 

Re-run the Playbook. You should observe that the host_vars "dns1" has higher priority than the group_vars "dns1" variable.

```bash
$ ansible-playbook exercise2b.yml 

PLAY [Exercise 2b] **********************************************************************

TASK [Print 'dns1' for gaia hosts] ******************************************************
[WARNING]: No inventory was parsed, only implicit localhost is available
ok: [pod1-gaia] => {
    "msg": "Primary DNS for host pod1-gaia is 172.31.0.2"
}
ok: [pod2-gaia] => {
    "msg": "Primary DNS for host pod2-gaia is 172.31.0.2"
}
ok: [pod3-gaia] => {
    "msg": "Primary DNS for host pod3-gaia is 172.31.0.2"
}
ok: [pod4-gaia] => {
    "msg": "Primary DNS for host pod4-gaia is 172.31.0.2"
}
ok: [pod5-gaia] => {
    "msg": "Primary DNS for host pod5-gaia is 8.8.8.8"      #### DIFFERENT DNS SERVER ####
}

PLAY RECAP ******************************************************************************
pod1-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod2-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod3-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod4-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod5-gaia                  : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

2c. Create the following subdirectories: cisco1, cisco2, cisco6 (inside the host_vars directory). The "host_vars/cisco5" subdirectory should already exist. Note, the directory names must exactly match the Ansible "inventory_hostname". In each of these ciscoX directories create a file named "ip_addresses.yml". Inside this file create a "loopback0" variable and assign this variable a unique IPv4 address (for example, 1.1.1.1 for cisco1).

Inside the same ciscoX directory, create a second file named "bgp.yml". In this file create a variable "bgp_router_id" and assign it a value of the "loopback0" variable you just created (remember your  "{{ loopback0 }}" notation). The "cisco5" bgp.yml file should contain both the "bgp_asn" and the "bgp_router_id".

Finally, modify your Playbook such that your output looks similar to the following.
TASK [Print BGP ASN for cisco hosts] **************************************************************************************************
ok: [cisco2] => {
    "msg": "The ASN for host cisco2 is 65001, the router-id is 2.2.2.2"
}
ok: [cisco1] => {
    "msg": "The ASN for host cisco1 is 65001, the router-id is 1.1.1.1"
}
ok: [cisco6] => {
    "msg": "The ASN for host cisco6 is 65001, the router-id is 6.6.6.6"
}
ok: [cisco5] => {
    "msg": "The ASN for host cisco5 is 65535, the router-id is 5.5.5.5"
}

The above exercise demonstrates that you can store additional inventory variables in host_vars, and group_vars. These subdirectories also allow you to divide your YAML into multiple files which can simplify inventory management.

