###

Create a role named 'address_range'. 

This role should configure three address ranges. The address ranges should be stored as a variable(s) in ./vars/main.yml (in the role).

The 'tasks/main.yml' should contain only two tasks: 

```yaml
- name: Configure Address Ranges
  ansible.builtin.import_tasks: cfg_address_ranges.yml
- name: Display Address Ranges
  ansible.builtin.import_tasks: display_address_ranges.yml
```

The tasks specified in 'cfg_address_ranges.yml' should configure the three address ranges that are stored in ./vars/main.yml.

The tasks specified in 'display_address_ranges.yml' should retrieve and display the currently configured address ranges.

You should create and use a handler in 'handlers/main.yml' to execute a publish action if the 'cfg_address_ranges.yml' results in a change.

