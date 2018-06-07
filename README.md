[![Build Status](https://travis-ci.org/EVasseure/cprint.svg?branch=master)](https://travis-ci.org/EVasseure/cprint)

## Cprint

Do you find it annoying when you have to search for a certain debug, or error, line in your console? Have you ever dreamed of a simple and quick way to make your debug print truly visible? Well here is your solution !  
cprint is a minimalist python library which gives you the possibility to print in color.  

## Install

pip install cprint

## Usage

```python
from cprint import _cprint

_cprint(arg) 							# WHITE
_cprint.ok(arg)							# BLUE
_cprint.info(arg)						# GREEN
_cprint.warn(arg)						# YELLOW
_cprint.err(arg, interrupt=False)		# BROWN
_cprint.fatal(arg, interrupt=False)		# RED
```

![Demo](/img/screen.png)
