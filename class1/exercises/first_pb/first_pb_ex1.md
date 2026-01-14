1a. Create an Ansible playbook with a single play and a single task. The play should execute against the 'local' group. The
task should use the "debug" module to print out a message.

1b. Execute your playbook and verify it executes correctly.

```bash
$ ansible-playbook first_pb_ex1.yml 

PLAY [First playbook] ********************************************************************

TASK [Gathering Facts] *******************************************************************
ok: [localhost]

TASK [Task1] *****************************************************************************
ok: [localhost] => {
    "msg": "Hello world"
}

PLAY RECAP *******************************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

```
