import re


def pct_change(old, new):
    """@todo: Docstring for pct_change.

    :old: @todo
    :new: @todo
    :returns: @todo

    """
    return (new - old) / old * 100
    # return (new != 0 and (new - old) / old * 100) or new


def flatten_expressions(expressions, sep=r'\s*;\s*'):
    """@todo: Docstring for flatten_expressions.

    :expressions: @todo
    :returns: @todo

    """
    expr_list = map(lambda x: x,
                    re.split(sep, ';'.join(expressions)))
    return expr_list
