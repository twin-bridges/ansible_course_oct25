### FW Policy Exercise

### Must add Ansible Management Rules to policy before doing this (see below)!!!
1. Use the 'check_point.mgmt.cp_mgmt_host' module to create a host object for 'Corp Web Server' with an IP address of '172.31.144.220'. Publish this change using a handler.
2. Use the 'check_point.mgmt.cp_mgmt_access_rule' module to add a firewall rule at position "1" specifying that "Any" source can reach the DMZ "Corp Web Server" for "http" and "https" services. Use handler to both publish this change and to install the new firewall policy.

### Process for adding Ansible Management Rules

```bash
$ cd ~/ansible_course_jan26/class3/mgmt_cfg/
$ nano add_mgmt_objects.yml   # Change to your pod, 'podX-mgmt'
$ nano fw_mgmt_policy.yml     # Change to your pod, 'podX-mgmt'
$ ansible-playbook add_mgmt_objects.yml
$ ansible-playbook fw_mgmt_policy.yml
```

Verify mgmt and gaia access still works (you can do this by re-running a Gaia and Mgmt
show playbook.
