# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib

path = pathlib.Path.cwd()

for filepath in path.iterdir():
    if filepath.is_dir():
        print(f"{' ':>10}{filepath.name}")
        for filepath in filepath.iterdir():
            if filepath.suffix == ".py":
                print(f"{' ':>20}{filepath.name}")
