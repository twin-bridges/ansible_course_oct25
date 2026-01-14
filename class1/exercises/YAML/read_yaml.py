#!/usr/bin/env python3
import yaml
from rich import print

f_name = input("Enter YAML filename: ")
with open(f_name) as f:
    data = yaml.safe_load(f)

print()
print(data)
print()
