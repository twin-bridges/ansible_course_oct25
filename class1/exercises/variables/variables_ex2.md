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

2c. Create the following subdirectories: pod1-gaia, pod2-gaia, pod3-gaia, pod4-gaia (inside the host_vars directory). The "host_vars/pod5-gaia" subdirectory should already exist. 

Note, the directory names must exactly match the Ansible "inventory_hostname". 

In each of these podX-gaia directories create a file named "ip_addresses.yml". Inside this file create a "eth1" variable and assign this variable a unique IPv4 address (for example, 1.1.1.1 for pod1-gaia).

Inside "pod5-gaia" directory, ensure the file named "dns.yml" exists and assigns "dns1" a value of "8.8.8.8". The rest of the "podX-gaia" hosts should rely on the groups_vars/gaia/dns.yml entry (which should assign "dns1" a value of "172.31.0.2"). The "pod5-gaia" should also have a file "ip_addresses.yml" with an entry for "eth1" (once again "eth1" should be assigned a unique, fictional IPv4 address).

Finally, modify your Playbook such that your output looks similar to the following.

```bash
$ ansible-playbook exercise2c.yml 

PLAY [Exercise 2c] ********************************************************************

TASK [Print 'dns1' and 'eth1' IP address for gaia hosts] ******************************
ok: [pod1-gaia] => {
    "msg": "\"Primary DNS for host pod1-gaia is 172.31.0.2\"\n\"The 'eth1' interface IP (fictional) is 1.1.1.1\"\n"
}
ok: [pod4-gaia] => {
    "msg": "\"Primary DNS for host pod4-gaia is 172.31.0.2\"\n\"The 'eth1' interface IP (fictional) is 4.4.4.4\"\n"
}
ok: [pod5-gaia] => {
    "msg": "\"Primary DNS for host pod5-gaia is 8.8.8.8\"\n\"The 'eth1' interface IP (fictional) is 5.5.5.5\"\n"
}
ok: [pod2-gaia] => {
    "msg": "\"Primary DNS for host pod2-gaia is 172.31.0.2\"\n\"The 'eth1' interface IP (fictional) is 2.2.2.2\"\n"
}
ok: [pod3-gaia] => {
    "msg": "\"Primary DNS for host pod3-gaia is 172.31.0.2\"\n\"The 'eth1' interface IP (fictional) is 3.3.3.3\"\n"
}

PLAY RECAP ****************************************************************************
pod1-gaia   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod2-gaia   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod3-gaia   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod4-gaia   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
pod5-gaia   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

Which of the above variables are being pulled from group_vars versus host_vars? If there is a conflict between group_vars and host_vars which variable wins?


