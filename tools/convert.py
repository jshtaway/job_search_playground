import os
import re

class MyCoolDict(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(MyCoolDict, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    if isinstance(v, dict):
                        self[k] = MyCoolDict(v)
                    elif isinstance(v, list):
                        self[k] = [MyCoolDict(item) for item in v]
                    else:
                        self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(MyCoolDict, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(MyCoolDict, self).__delitem__(key)
        del self.__dict__[key]


def to_camel_case(my_str):
    """
    Converts a string to camel case.

    Args:
        my_str (str): The string to convert.

    Returns:
        str: The camel case version of the input string.
    """
    my_str = re.sub(r"(_|-)+", " ", my_str)
    my_str = ' '.join(re.findall('[A-Z][^A-Z]*', my_str))
    my_str = my_str.split()
    my_str = [word.capitalize() for word in my_str]
    return ''.join([my_str[0].lower()] + my_str[1:])

def to_title_string(my_str):
    my_str = re.sub(r"(_|-)+", " ", my_str)
    my_str = ' '.join(re.findall('[A-Z][^A-Z]*', my_str))
    return my_str.capitalize()