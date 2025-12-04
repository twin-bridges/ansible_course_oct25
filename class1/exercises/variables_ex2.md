1a. Create a Playbook containing a Play that executes on the "arista5" host. Ensure that "gather_facts" is set to True. Create a task that uses the "debug" module to print the "ansible_facts" to stdout. Create a subsequent task that prints just "ansible_facts.net_all_ipv4_addresses" to stdout.

Note: Ansible changed the behavior of network fact gathering reducing the amount of facts gathered by default. For all the parts of exercise1, you should add the following play-level arguments so that all of the needed network facts are gathered.
gather_facts: True
gather_subset: all

1b. Add tasks to your Playbook to print out inventory information about arista5. This should include both the "ansible_network_os" and the "ansible_host" variables.

1c. Create a directory called "group_vars" in the same directory as your Playbook. Within this directory, create a file named "all.yml". In this file, define a variable named "desired_eos_version" and set it to a value of "4.18.3". Add another task to your Playbook to print out the value of this "desired_eos_version" variable.

1d. In the same directory as your Playbook, create a YAML file called "my_vars.yml". Within this file, create the same variable named "desired_eos_version" as in the previous exercise, but with a different value. Load this variable from my_vars.yml by adding "vars_files: my_vars.yml" into your Playbook. Re-run the Playbook to see what happens. Which "desired_eos_version" wins? Why?

1e. Add a task to your playbook to create a new variable using "set_fact". Name this variable "device_hostname" and set the value of it equal to the "inventory_hostname" combined with the suffix ".lab.io". In a final task, print the value of this variable.


2a. Create a new directory that includes a Playbook and a "group_vars" directory. The group_vars directory should contain a "cisco" subdirectory. Inside this "group_vars/cisco" subdirectory, create a file named "bgp.yml". Inside this "bgp.yml" file create a variable for "bgp_asn" and assign it a value between 65000 and 65535. Use the "debug" module to print a message to stdout. The message should look similar to the following:
TASK [Print BGP ASN for cisco hosts] **************************************************************************************************
ok: [cisco1] => {
    "msg": "The ASN for host cisco1 is 65001"
}
ok: [cisco5] => {
    "msg": "The ASN for host cisco5 is 65001"
}
ok: [cisco2] => {
    "msg": "The ASN for host cisco2 is 65001"
}
ok: [cisco6] => {
    "msg": "The ASN for host cisco6 is 65001"
}

2b. Create a "host_vars" directory, and a subdirectory named "cisco5" within it. Inside this, "host_vars/cisco5", create a file named "bgp.yml". Inside this file, create a variable named "bgp_asn" using a different ASN value. Re-run the Playbook. You should observe that the host_vars "bgp_asn" has higher priority than the group_vars "bgp_asn" variable.

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

