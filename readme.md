# python-logger
## About

This is a basic logging module for python built in python. It is much more simple than the built in python 3 one.

## Contents of this Repository
`logger_example.py` - A piece of example code that uses every function and mode of the module  
`logger.py` - The module itself  
`readme.md` - This File  
`run.log` - An example log file that you would get printed out from `logger_example.py`  

## Modes
`disabled` - Disables the logger so it will return no output  
`terminal` - Outputs logs only to the terminal  
`file` - Outputs logs only to a text file  
`file_terminal` - Outputs to both the terminal and a text file  

## Functions and Variables
### Functions
`error(msg)` - Outputs an Error with the message `msg`  
`warn(msg)` - Outputs a Warning with the message `msg`  
`info(msg)` - Outputs Information with the message `msg`  
`mode_update(new_mode)` - Changes the mode. see **Modes**  

### Variables
`LOG_FILE` - By default it's value is `"run.log"`. It dictates what file the file output will output to. Must be a `str` value.  
