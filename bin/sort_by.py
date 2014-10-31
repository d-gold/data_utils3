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
from lib.d3_utils import pct_change, flatten_expressions

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
    parser.add_argument('-f', '--fields',
                        dest='fields',
                        default=None,
                        required=True,
                        action='append',
                        help='XXX'
                        'XXX')
    parser.add_argument('--asc', '--ascending',
                        dest='ascending',
                        default=True,
                        required=False,
                        action='store_true',
                        help='XXX'
                        'XXX')
    parser.add_argument('--desc', '--descending',
                        dest='ascending',
                        required=False,
                        action='store_false',
                        help='XXX'
                        'XXX')


    return parser


def main():
    """@todo: Docstring for main.

    :returns: @todo

    """

    def sort_data(columns, ascending, dataset):
        """@todo: Docstring for sort_data.

        :columns: @todo
        :ascending: @todo
        :dataset: @todo
        :returns: @todo

        """
        return dataset.sort(columns=columns, ascending=ascending)

    parser = get_argument_settings()
    args = parser.parse_args()

    delimiter = args.delimiter
    field_list = flatten_expressions(args.fields, sep=r'\s*[,;]\s*')

    input_files = args.input_files or [sys.stdin]
    data = map(F(load_datasets, delimiter), input_files)

    transformed = map(F(sort_data, field_list, args.ascending), data)

    result = save_datasets(transformed, args.output_file, delimiter=delimiter)
    return result


if __name__ == '__main__':
    main()
