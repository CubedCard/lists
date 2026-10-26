import os
import toml

DIR_NAME = f"{os.getcwd()}/list"

for filename in os.listdir(DIR_NAME):
    with open(os.path.join(DIR_NAME, filename), "r") as f:
        config = toml.load(f)
        for wish in config["Tim"]["items"]:
            print(wish)
