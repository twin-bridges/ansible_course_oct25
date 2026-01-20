### Add network objects exercise

Create a playbook that executes against your Pod in the lab. The playbook should configure the following network objects:

      name: Voice Network
      network: 10.200.10.0/24

      name: IT Mgmt
      network: 10.200.11.0/24

      name: OOB Access Network
      network: 198.51.100.0/26

The playbook should use a single task and a loop to configure the above objects. You should use the 'check_point.mgmt.cp_mgmt_network' module.

Use a handler when configuring the above three network objects such that any change in a network object causes the firewall publish handler to execute.

