# AirBnb_clone

![hbnb](https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## Table of Contents

* [Description](#description)
* [Purpose](#purpose)
* [Requirements](#requirements)
* [File Structure](#file-structure)
* [Usage](#usage)
* [Examples](#examples)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Description

**hbnb** is a full clone of the web application AirBnB. This clone will be constructed in five phases. Currently, we have completed the first phase - to build a simple command interpreter that parses and evaluates input from the commandline appropriately. Test suite included. Future steps to come.

## Purpose

The purpose of the AirBnb project is to:
* create a parent class BaseModel that will take care of initialization, serialization, and deserialization of future instances
* create a simple flow of serialization/deserialization: instance <-> dictionary <-> JSON string <-> file
* create all classes used for AirBnb that inherit from BaseModel
* create an abstracted storage engine (FileStorage)
* create unittests to validate all our classes and storage engine
* create a command interpreter that can do the following:
  * create a new object
  * retrieve an object from a file, database, etc.
  * do operations on objects
  * update attributes of an object
  * destroy an object
* learn how to do the following:
  * create a Python package
  * create a command interpreter in Python using the cmd module
  * implement Unit testing on a large project
  * serialize and deserialize a class
  * write and read a JSON file
  * manage datetime
  * create UUIDs
  * use *args and **kwargs
  * handle named arguments in a function

## Requirements

* Must follow [Betty](https://github.com/holbertonschool/Betty/wiki) style and document guidelines
* Allowed editors: `vi`, `vim`, `emacs`
* Must have a `README.md` file
* All header files must be include guarded
* No more than 5 functions per files
* Must have documentation
* Must have unittests that can be executed using `python3 -m unittest discover tests`

## File Structure

* [AUTHORS](AUTHORS) - list of contributors
* [console.py](console.py) - command interpreter
  * `do_create` - create a new instance of a class
  * `do_show` - prints string representation of an instance based on class name and id
  * `do_all` - prints all string representation of all instances based or not on the class name
  * `do_destroy` - deletes an instance based on the class name and id
  * `do_update` - updates an instance based on the class name and id by adding or updating attribute
  * `emptyline` - ensures that hitting 'enter' will not remember the last command
  * `do_quit` - quit program
  * `do_EOF` - exit at end of file
* [file_storage.py](/models/engine/file_storage.py) - class FileStorage
  * `all` - returns the dictionary __objects
  * `new` - sets in __objects the obj with key <obj class name>.id
  * `save` - serializes __objects to the JSON file (path: __file_path)
  * `reload` - deserializes the JSON file to __objects
* [base_model.py](/models/base_model.py) - parent class that will take care of initialization/serialization/deserialization of future instances
  * `__init__` - initialize instance attributes
  * `__str__` - creates formatted string representation of instance
  * `__repr__` - returns string representation of instance
  * `save` - updates public instance attribute updated_at with current datetime
  * `to_dict` - creates a dictionary containing all keys/values of `__dict__` of the instance
* [user.py](/models/user.py) - class User
* [city.py](/models/city.py) - class City
* [state.py](/models/state.py) - class State
* [place.py](/models/place.py) - class Place
* [review.py](/models/review.py) - class Review
* [amenity.py](/models/amenity.py) - class Amenity
* [`__init__.py`](/models/__init__.py) - initialization code for Python package models
* [tests](/tests/) - unit test files

## Execution

### Unit Testing

```python3 -m unittest discover tests```

### Console

```./console.py```

## Usage Examples

### Interactive Mode

```c
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-Interactive Mode

```c
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Bugs

At this time, there are no known bugs.

## Authors

* Nick Teixeira | [GitHub](https://github.com/nickolasteixeira) | [Twitter](https://twitter.com/NTTL_LTTN)
* Becky Chen | [GitHub](https://github.com/bchen528) | [Twitter](https://twitter.com/bchen803)

## License

**hbnb** is open source and free to download and use
