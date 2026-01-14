1a. Create a list in YAML. Use the Python script "read_yaml.py" to read the YAML file and to verify your data structure.

```bash
# Example output
$ ./read_yaml.py 
Enter YAML filename: yaml_ex1a.yml

['mun-fw1', 'mun-fw2', 'col-fw1', 'col-fw1']
```

1b. Create a dictionary in YAML. Use the Python script "read_yaml.py" to read the YAML file and to verify your data structure.

```bash
# Example output
$ ./read_yaml.py 
Enter YAML filename: yaml_ex1b.yml

{
    'host': 'chkpnt-pod1.lasthop.io',
    'device_type': 'checkpoint_gaia',
    'username': 'admin',
    'use_keys': True,
    'key_file': '/home/kbyers/.ssh/eu-sshkey.pem'
}
```

1c. Repeat the dictionary except use the YAML compressed format for the dictionary. Once again use "read_yaml.py" to read the YAML file and to verify your data structure.

```bash
# Example output
# Python output will be the same as exercise 1b.
$ ./read_yaml.py 
Enter YAML filename: yaml_ex1c.yml

{
    'host': 'chkpnt-pod1.lasthop.io',
    'device_type': 'checkpoint_gaia',
    'username': 'admin',
    'use_keys': True,
    'key_file': '/home/kbyers/.ssh/eu-sshkey.pem'
}
```
