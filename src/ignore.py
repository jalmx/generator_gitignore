#!/usr/bin/env python3

from urllib.request import urlopen
from sys import argv, exit

HELP = """
USAGE:
    ignore [languaje]

    ignore python 
    
    ignore node

    All gitignore from https://github.com/github/gitignore
"""

langs = {
        "python":"https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore",
        "node": "https://raw.githubusercontent.com/github/gitignore/main/Node.gitignore"
        }


def get_ignore(name:str):
    ignore = ""
    with urlopen(langs[name]) as response:
        text = response.read().decode("utf-8")
        ignore = text
        print("Downloaded")

    with open(".gitignore","+w",encoding="utf-8") as file:
        file.write(ignore)
        print(f"Added .gitignore for {name}")


def cli():
    if len(argv) < 2 or len(argv) > 2:
        print(HELP)
        exit(1)

    lang = argv[1]
    
    if lang == "--help":
        print(HELP)
        exit(0)
    
    try:
        get_ignore(lang)
    except Exception as e:
        print(e)
        print(HELP)
        exit(1)
    
    exit(0)

def main():
    cli()

if __name__ == "__main__":
    main()
