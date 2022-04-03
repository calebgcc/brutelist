# Brutelist

Brutelist is a simple python script designed to automate the creation of seed-based dictionary attack files (sensitive information collected during a CTF or penetration test)


## Installation
To run brutelist you will need Python 3.7 or later.
Simply clone the repository:
```bash
git clone https://github.com/calebgucciardi/brutelist.git
cd brutelist/
python3 brutelist.py --help
```

## Getting Started
To use brutelist you will need a `template file` and a `seed list`

#### Seed List
Brutelist is designed to be a useful tool during a CTF. Often names and sensitive information are collected that can lead to passwords to move on to the next step.
The brutelist seed list is simply a file (or list passed as an argument) of this information.

#### Template file
The template file is used to add common patterns to each seed list item, for example it is common for a password to be a name + 123, so in our template file we will have an entry like this: `{}123` where `{}` will be replaced by each seed list entry  

#### Example
```bash
python3 brutelist.py -t template -o dictionary_output -l admin foo bar
```
