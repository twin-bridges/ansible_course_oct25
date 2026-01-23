### Main Project Exercise

You should use roles for this exercise.
* You should have a separate role for Gaia.
* You should have separate roles for the Mgmt Objects and for the FW Policy.
* You should use a shared role for handlers (which would be a required dependency for your other roles in meta/main.yml).

### Gaia Configuration
* The Gaia Configuration role (tasks/main.yml) should use either import_tasks or include_tasks to include/import static_routes.yml and dns.yml (for the static route configuration and DNS configuration specified below).
* Configure a static route for 172.31.128.0/21, interface "eth1", next hop 172.31.128.1
* Configure the following DNS Settings:
  * DNS1: "172.31.0.2"
  * DNS2: "8.8.8.8"
  * DNS3: "8.8.4.4"
  * DNS Domain: lasthop.io
* Configure the DNS domainname using 'clish -c "set domainname lasthop.io"' and the 'cp_gaia_run_script' module.

Notes: try to ensure you decouple your tasks from your data. In other words, the specifics of the static route and of the DNS settings should be stored as role variables (and not directly hard-coded in the tasks).

### Mgmt Object Configuration
Host Objects
* Ansible Server, 3.125.34.232
* Windows SmartConsole, 172.31.12.101
* Windows SmartConsole Public, 3.71.9.240

Network Objects (with NAT auto hide behind the gateway)
* hq_net_128, 172.31.128.0/24
* hq_net_129, 172.31.129.0/24
* hq_net_130, 172.31.130.0/24
* hq_net_131, 172.31.131.0/24
* hq_net_132, 172.31.132.0/24
* hq_net_133, 172.31.133.0/24
* hq_net_134, 172.31.134.0/24
* hq_net_135, 172.31.135.0/24

DMZ Object (additional Host Object)
* Corp Web Server, 172.31.144.220

Once again you should use import_tasks/include_tasks from your main.yml file to import/include the mgmt host object, the network objects, and the DMZ objects.

### FW Policy Configuration

First configure management access from the Ansible Server and SmartConsole to not lock yourself out from the Ansible Server.

Allow "Any" access to the firewall/mgmt server itself from the following:
* Ansible Server
* Windows SmartConsole
* Windows SmartConsole Public

Also allow "Any", SSH access to the firewall itself (so we can SSH directly into clish/expert mode). AWS firewall has separate access restrictions.

Publish and Install your changes.

Second, configure HTTP/HTTPS access from Any source to "Corp Web Server" on the DMZ. Publish and Install your changes.

I recommend you separate the Mgmt Policy and the DMZ Policy into two separate task files that you import/include from tasks/main.yml

### Try to ensure that your entire playbook (all your roles) are idempotent.

Note, in order to make the 'clish -c "set domainname lasthop.io"' task idempotent, you will need to:
1. First retrieve the current configuration.
2. Add logic to your 'cp_gaia_run_script / set domainname' task whereby the script execution only happens if the domainname of 'lasthop.io' has not been configured.

### Tags

Use tags so that the Gaia config, network and host objects, and firewall policy can be configured independently.

### Vault

Use vault to encrypt your 'ansible_username' and 'ansible_password' inside either 'group_vars/all.yml' or inside a role variable 'defaults/main.yml'. The location you use will depend on whether you use import_role or include_role.

### Bonus / Optional
Create a separate role named 'script_b64_decode' that takes the output of the 'cp_mgmt_run_script' module execution, parses this output, and returns the decoded responseMessage.

Execution of this role should look similar to the following:

```yaml
- name: Use 'script_b64_decode' role to extract responseMessage
  ansible.builtin.include_role:
    name: script_b64_decode
  vars:
    # Pass the required variable into the role
    script_b64_decode_input: "{{ response }}"

- name: Display the decode responseMessage
  ansible.builtin.debug:
    var: script_b64_decode_rm
```

The above '{{ response }}' variable is the response from a 'cp_mgmt_run_script' execution. 

The 'script_b64_decode_rm' variable is set in the role and is the decoded responseMessage.

