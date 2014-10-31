#!/usr/bin/env python
# encoding: utf-8

# pylint: disable=W0110, W0614, W0141, C0103

import sys
import re
import textwrap
from fn import F
from lib.parse_args import add_common_arguments
from lib.d3_fn import cons
from lib.d3_io import load_datasets, save_datasets
from lib.d3_utils import pct_change, flatten_expressions
import numpy as np

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
    parser.add_argument('--oc', '--output-columns',
                        dest='output_columns',
                        default=None,
                        required=False,
                        action='append',
                        help='XXX'
                        'XXX')

    parser.add_argument('--cw', '--output-columns-widths',
                        dest='column_widths',
                        default=None,
                        required=False,
                        action='append',
                        help='XXX'
                        'XXX')

    parser.add_argument('-m', '--monkey-readable',
                        dest='monkey_readable',
                        default=False,
                        required=False,
                        action='store_true',
                        help='XXX'
                        'XXX')

    return parser


def main():
    """@todo: Docstring for main.

    :returns: @todo

    """

    parser = get_argument_settings()
    args = parser.parse_args()

    delimiter = args.delimiter
    output_columns = (args.output_columns and flatten_expressions(args.output_columns, sep=r'\s*[,;]\s*')) or None
    column_widths = (args.column_widths and flatten_expressions(args.column_widths, sep=r'\s*[,;]\s*')) or None
    column_widths = (column_widths and map(lambda x: re.split('\s*:\s*', x), column_widths)) or None
    if column_widths:
        d = {}
        for k, v in column_widths:
            d[k] = v
        column_widths = d
    else:
        column_widths = {}

    input_files = args.input_files or [sys.stdin]
    data = map(F(load_datasets, delimiter), input_files)

    result = save_datasets(data, args.output_file,
                           delimiter=delimiter,
                           monkey_readable=args.monkey_readable,
                           columns=output_columns,
                           column_widths=column_widths)

    return result


if __name__ == '__main__':
    main()


