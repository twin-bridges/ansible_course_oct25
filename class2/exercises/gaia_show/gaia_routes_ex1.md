
Create an Ansible playbook that connects to the Gaia host of your pod. In this playbook do the following:
1. Use the 'check_point.gaia.cp_gaia_routes_facts' module to retrieve the Gaia routing table.
2. Iteratively use the 'ansible.builtin.debug' and 'ansible.builtin.set_fact' modules to display and extract certain information from the returned routing table (namely extract the default route and the corresponding 'gateways' information).
3. Use a final 'ansible.builtin.debug' task to print the default route and the next_hop out (the next_hop is the 'gateways' information). Your output should look similar to the following:

```bash
ansible-playbook gaia_routes_ex1.yml

PLAY [Inspect Routes] *********************************************************************

TASK [Inspect Routes] *********************************************************************
[WARNING]: No inventory was parsed, only implicit localhost is available
ok: [pod1-gaia]

TASK [Extract the route_table] ************************************************************
ok: [pod1-gaia]

TASK [Create prefix and next_hop variables from route_table (default route)] **************
ok: [pod1-gaia]

TASK [Display prefix and next_hop variables for the default route] ************************
ok: [pod1-gaia] => {
    "msg": "\"Prefix: 0.0.0.0\"\n\"Next Hop: [{'address': '172.31.32.1', 'interface': 'eth0'}]\"\n"
}

PLAY RECAP ********************************************************************************
pod1-gaia   : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```
