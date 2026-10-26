import os
import toml

DIR_NAME = f"{os.getcwd()}/list"
ITEMS_HEADER = "items"

for filename in os.listdir(DIR_NAME):
    with open(os.path.join(DIR_NAME, filename), "r") as f:
        config = toml.load(f)
        for person in config:
            print(f"-------------------\n{person}\n-------------------")
            for wish in config[person][ITEMS_HEADER]:
                print(wish)
            print(f"-------------------\n")
