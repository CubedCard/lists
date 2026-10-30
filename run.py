import os
import toml
import yaml
import pandas as pd
from tabulate import tabulate

DIR_NAME = f"{os.getcwd()}/list"
ITEMS_HEADER = "items"
CONFIG_FILENAME = "config.yaml"

for filename in os.listdir(DIR_NAME):
    with open(os.path.join(DIR_NAME, filename), "r") as f:
        config = toml.load(f)
        for person in config:
            print(f"-------------------\n{person}\n-------------------")
            wishes = config[person][ITEMS_HEADER]
            df = pd.DataFrame([wishes])
            print(tabulate(df, tablefmt='psql'))


def read_config():
    with open(CONFIG_FILENAME, "r") as file:
        loaded_data = yaml.safe_load(file)

    if not loaded_data:
        raise FileNotFoundError(f"Failed to load config from {CONFIG_FILENAME}")

    print(f"Config loaded from {CONFIG_FILENAME}")
    print(loaded_data)


read_config()
