LITSLIST
========

Clone this repository

```
$ git clone https://github.com/AlexMathew/litslist
$ cd litslist
```

Or download and extract the zip file.

Download the dependencies.

```
$ pip install -r requirements.txt 
```

Setup the package.

```
$ python setup.py install
```

This sets up the `litslist` command. 

```
$ litslist --help
```

Use the `create` command to create the required number of sets.

```
$ litslist create 30
```

Creates a 'Lists' folder with 30 sets. Creates 'Remaining_*' files for the unused items in the lists. Also sets up Sets.csv, which can be saved as an Excel file.
