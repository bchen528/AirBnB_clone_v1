# AirBnB_clone_v1: Console and web static

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

**hbnb** is a full-stack clone of the web application [AirBnB](https://www.airbnb.com/). This clone was built in four iterative phases. This version includes completion of Phase 1, which has two parts: building 1) a command interpreter that parses and evaluates input from the commandline appropriately and 2) a landing page. Test suite included. 

### Part 1: Build a command-line interpreter that handles AirBnB objects
![console](https://i.imgur.com/RU67f06.png)

### Part 2: Create a landing page
![webstatic_diagram](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)

**Links to other versions:**
* [AirBnB_clone_v2: MySQL, Deploy static, Web framework](https://github.com/bchen528/AirBnB_clone_v2)
* [AirBnB_clone_v3: RESTful API](https://github.com/bchen528/AirBnB_clone_v3)
* [AirBnB_clone_v4: Web dynamic](https://github.com/bchen528/AirBnB_clone_v4) (Final version!)

## Purpose

The purpose of Phase 1 is to:
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
 * [web_static](web_static) - contains HTML, CSS, and images files
   * [0-index.html](web_static/0-index.html) - a basic HTML page that contains a header and footer like below:
   ![0-index.html](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/0-index.png)
  
   * [1-index.html](web_static/1-index.html) - an HTML page that displays a header and a footer by using the style tag in the head tag (same display as 0-index.html)

   * [2-index.html](web_static/2-index.html) - an HTML page that displays a header and a footer by using CSS files (same display as 1-index.html)

   * [3-index.html](web_static/3-index.html) - an HTML page that displays a header and footer by using CSS files to display like below:
   ![3-index.html](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/3-index.png)

   * [4-index.html](web_static/4-index.html) - an HTML page that displays a header, footer and a filters box with a search button
   ![4-index.html](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/4-index.png)

   * [5-index.html](web_static/5-index.html) - an HTML page that displays a header, footer and a filters box
   ![5-index.html](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/5-index.png)

   * [6-index.html](web_static/6-index.html) - an HTML page that displays a header, footer and a filters box with dropdown
   ![6-index.html_part1](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/6-index_0.png)
   ![6-index.html_part2](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/6-index_1.png)

   * [7-index.html](web_static/7-index.html) - an HTML page that displays a header, footer, a filters box with dropdown and results
   ![7-index.html](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/7-index.png)

   * [8-index.html](web_static/8-index.html) - an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search
   ![8-index.html](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png)
   
   * [101-index.html](web_static/101-index.html) - an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search, uses Flexible boxes for all Place articles (same display as 8-index.html)
   
   * [102-index.html](web_static/101-index.html) - an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search; uses Flexible boxes for all Place articles; has responsive design (same display as 8-index.html)
   * [styles](web_static/styles) - contains CSS files
      * [2-common.css](web_static/styles/2-common.css) - global (i.e. body) style
      * [2-header.css](web_static/styles/2-header.css) - header style
      * [2-footer.css](web_static/styles/2-footer.css) - footer style
      * [3-common.css](web_static/styles/3-common.css) - body style
      * [3-header.css](web_static/styles/3-header.css) - header style
      * [3-footer.css](web_static/styles/3-footer.css) - footer style
      * [4-common.css](web_static/styles/4-common.css) - body style
      * [4-filters.css](web_static/styles/4-filters.css) - filters style
      * [5-filters.css](web_static/styles/5-filters.css) - filters style
      * [6-filters.css](web_static/styles/6-filters.css) - filters style
      * [7-places.css](web_static/styles/7-places.css) - places style
      * [8-places.css](web_static/styles/8-places.css) - places style
      * [101-places.css](web_static/styles/101-places.css) - places style
      * [102-places.css](web_static/styles/102-places.css) - places style

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
