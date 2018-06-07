# coding: utf8

from .cprint import cprint
from .Cprint import Cprint


_cprint = cprint
cprint = Cprint().cprint()

"""
    This module give to possibility to print in color.
"""
