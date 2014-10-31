#!/usr/bin/env python
# encoding: utf-8

# pylint: disable=W0110, W0614, W0141, C0103

import sys
import re
import textwrap
from fn import F
from lib.parse_args import add_common_arguments
from lib.d3_fn import cross_flist
from lib.d3_io import load_datasets, save_datasets
from lib.d3_utils import pct_change

from math import *


def get_argument_settings():
    """@todo: Docstring for get_argument_settings.

    :returns: @todo

    """
    description = textwrap.dedent("""
    Joins two delimited files by common keys.
    """)

    epilog = textwrap.dedent("""

    Examples:

    """)

    m_overrides = []
    parser = add_common_arguments(m_overrides, description=description,
                                  epilog=epilog)
    parser.add_argument('-x', '--expresssion',
                        dest='expression',
                        default=None,
                        required=True,
                        action='append',
                        help='XXX'
                        'XXX')

    return parser


def main():
    """@todo: Docstring for main.

    :returns: @todo

    """

    def apply_add_column(x, expression):
        """@todo: Docstring for apply_add_column.

        :dataset: @todo
        :expression: @todo
        :returns: @todo

        """
        x[expression[0]] = eval(expression[1])
        return x

    parser = get_argument_settings()
    args = parser.parse_args()

    delimiter = args.delimiter
    expression_list = map(lambda x: re.split(r'\s*[:=]\s*', x, 1),
                          re.split(r'\s*;\s*', ';'.join(args.expression)))
    # TODO: Apply built in functions here.
    eval_list = map(lambda x:
                    (x[0], re.sub(r'<(\S+)>', "x['\\1']",
                                  re.sub(r'\[(\S+)\]', "x['\\1']", x[1]))),
                    expression_list)

    input_files = args.input_files or [sys.stdin]
    data = map(F(load_datasets, delimiter), input_files)

    transformed = cross_flist(apply_add_column, data, eval_list)

    result = save_datasets(transformed, args.output_file, delimiter=delimiter)
    return result


if __name__ == '__main__':
    main()
