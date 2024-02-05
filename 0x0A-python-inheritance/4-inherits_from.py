#!/usr/bin/python3
"""Module with method inherits_from"""


def inherits_from(obj, a_class):
    """Return:
    True: if the object is exactly an instance of the specified class
    if the object is an instance of a class that inherited from,
    the specified class
    otherwise:false"""
    return isinstance(obj, a_class) and type(obj) != a_class
