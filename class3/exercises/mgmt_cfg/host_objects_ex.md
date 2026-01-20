### Add host objects exercise

Create a playbook that executes against your Pod in the lab. The playbook should configure the following host objects (use module 'check_point.mgmt.cp_mgmt_host'):

        name: DMZ DB1
        ipv4_address: 172.31.144.241

        name: DMZ Email
        ipv4_address: 172.31.144.242

        name: DMZ Reporting
        ipv4_address: 172.31.144.243

Use a handler when configuring the above three host objects such that any change in a host object causes the firewall publish handler to execute.

