import yaml
from rich import print

f_name = input("Enter filename: ")
with open(f_name) as f:
    d = yaml.safe_load(f)

print(d)
