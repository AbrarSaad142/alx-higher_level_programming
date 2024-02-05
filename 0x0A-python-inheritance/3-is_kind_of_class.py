#!/usr/bin/python3
"""Module with method is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return:
    True: if the object is exactly an instance of the specified class
    if the object is an instance of a class that inherited from,
    the specified class
    otherwise:false"""
    return isinstance(obj, a_class)
