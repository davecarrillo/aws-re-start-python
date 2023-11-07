# import pyyaml module
import yaml
from yaml.loader import SafeLoader

def read_yaml_file(file_name):
    data=""
    try:
        with open(file_name) as f:
            data = yaml.load(f, Loader=SafeLoader)
    except IOError:
        print("Could not read file.")
    return data