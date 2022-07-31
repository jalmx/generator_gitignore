# gitignore generator

Script for generate a gitignore for python and node, is you have to add a new language add to script from page https://github.com/github/gitignore

## Usage

```bash
USAGE:
    ignore [language]

    ignore python 
    
    ignore node

    All gitignore from https://github.com/github/gitignore
```

## Install 

Just download and move to you want

```bash
wget -c https://raw.githubusercontent.com/jalmx/ignore_generator/master/bin/ignore
```

**Install to PATH**

```bash
wget -c https://raw.githubusercontent.com/jalmx/ignore_generator/master/bin/ignore -O $HOME/.local/bin/ignore
```

`Note: Change permission to exe`

```bash
sudo chmod +x ignore
```


## Build

```bash
./build.sh
```

*Require to build:*

pip install python-minifier
