1a. Create a Playbook containing a Play that executes on the "podx-gaia" host (where 'x' is your pod). Ensure that "gather_facts" is set to false. 

Create a task that uses the "debug" module to print the "ansible_facts" to stdout.

1b. Add tasks to your Playbook to print out inventory information about "podx-gaia". This should include both the "ansible_network_os" and the "ansible_host" variables.

1c. Create a directory called "group_vars" in the same directory as your Playbook. Within this directory, create a file named "all.yml". In this file, define a variable named "external_intf" and set it to a value of "eth1". Add another task to your Playbook to print out the value of this "external_intf" variable.

1d. In the same directory as your Playbook, create a YAML file called "my_vars.yml". Within this file, create the same variable named "external_intf" as in the previous exercise, but with a different value ("eth3" in this case). Load this variable from my_vars.yml by adding "vars_files: my_vars.yml" into your Playbook. Re-run the Playbook to see what happens. Which "external_intf" wins? Why?

1e. Add a task to your playbook to create a new variable using "set_fact". Name this variable "device_hostname" and set the value of it equal to the "inventory_hostname" combined with the suffix ".lab.io". In a final task, print the value of this variable.

