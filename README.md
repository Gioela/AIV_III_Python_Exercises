# **AIV III - Python Exercises**

## Info and details
This repository groups these kinds of arguments:
- first steps of Python class implementation
- override some Python class protocols
- use the pytest module
- use the TDD method

## Project Structure
The Project folder structure is defined by this head folders:
- core
- utils
- test

### _Core folder_
In core folder are all python exercises scripts.

### _Utils folder_
Here is a script with a class that has some useful class methods.
List and functionality of class methods:
- is_numeric: return True or False if a given value is numeric or not
- is_alpha_value: return True or False if a given value is composed by only and all char values
- is_float_value: return True if a given value could be cast to float. Otherwise,
raise ValueError
- is_int_value: return True if a given value could be cast to int. Otherwise,
raise ValueError
- is_value_type: return True if a given value could be cast to a specific given type.
Otherwise, raise ValueError or AssertionError

### _Test folder_
In this folder are all pytest scripts taht can be executed.