import os
import platform


def is_windows() -> bool:
    if os.name == 'nt':
        return True
    if platform.system() == 'Windows':
        return True
    return False


# https://github.com/bottlepy/bottle/commit/fa7733e075da0d790d809aa3d2f53071897e6f76
# https://github.com/pydanny/cached-property/blob/master/cached_property.py
class cached_property(object):  # noqa: N801
    """
    A property that is only computed once per instance and then replaces itself
    with an ordinary attribute. Deleting the attribute resets the property.
    """  # noqa

    def __init__(self, func):
        self.__doc__ = getattr(func, "__doc__")
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value