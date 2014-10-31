# pylint: disable=C0103

import config
import collections


identity = lambda x: x


def first(x):
    return (len(x) > 0 and x[0]) or None


def car(x):
    return (len(x) > 0 and x[0]) or ()


def cdr(x):
    return (len(x) > 1 and x[1:]) or ()


def cons(value, x):
    """@todo: Docstring for cons.

    :value: @todo
    :x: @todo
    :returns: @todo

    """
    return tuple(value) + tuple(x)


def do(f, x):
    """Execute a function with side-effects.

    :f: Function to execute.

    :returns: x

    This will call the function f(x) and return x. This is used in cases
    where you want to call f() for the purposes of its side-effects but do
    not want to use the return value of f().

    Example:
        do_something_with_x(do(print_info_about_x, calculate_x()))

    The print_info_about_x() function prints x, but doesn't do anything to it.
    We are only interested in print_info_about_x() for its side effects.
    The do() function should also make this chain o' functions composable.

    """
    f(x)
    return x


def monadic_print(x):
    """@todo: Docstring for monadic_print.

    :x: @todo
    :returns: @todo

    """
    print x
    return x


def is_seq(obj):
    """@todo: Docstring for is_seq.

    :seq: @todo

    :returns: @todo

    Tests to see if obj is a tuple, list or other sequence type object.
    This will exclude strings and dictionaries.

    """

    if isinstance(obj, basestring):
        return False

    if isinstance(obj, config.Sequence):
        return True
    return isinstance(obj, collections.Sequence)


def flist(f, x, y):
    """@todo: Docstring for flist.

    :f: @todo
    :x: @todo
    :returns: @todo

    """

    for i in y:
        x = f(x, i)
    return x


def cross_flist(f, x, y):
    """@todo: Docstring for cross_flist.

    :f: @todo
    :x: @todo
    :returns: @todo

    """

    results = []
    for i in x:
        for j in y:
            i = f(i, j)
        results.append(i)
    return results
