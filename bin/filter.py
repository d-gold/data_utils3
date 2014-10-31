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
    parser.add_argument('--and',
                        dest='use_and',
                        default=True,
                        required=False,
                        action='store_true',
                        help='XXX'
                        'XXX')
    parser.add_argument('--or',
                        dest='use_and',
                        required=False,
                        action='store_false',
                        help='XXX'
                        'XXX')

    return parser


def main():
    """@todo: Docstring for main.

    :returns: @todo

    """

    def apply_filter(x, expression):
        """@todo: Docstring for apply_add_column.

        :dataset: @todo
        :expression: @todo
        :returns: @todo

        """
        x = x[expression[0]] == eval(expression[1])
        return x

    parser = get_argument_settings()
    args = parser.parse_args()

    delimiter = args.delimiter
    expression_list = re.split(r'\s*;\s*', ';'.join(args.expression))
    # TODO: Apply built in functions here.
    eval_list = map(lambda x:
                    re.sub(r'<(\S+)>', "x['\\1']",
                           re.sub(r'\[(\S+)\]', "x['\\1']", x)),
                    expression_list)

    input_files = args.input_files or [sys.stdin]
    data = map(F(load_datasets, delimiter), input_files)
    use_and = args.use_and
    expression = (use_and and ' & '.join(eval_list)) or \
                 ' | '.join(eval_list)

    transformed = []

    for x in data:
        filtered = x.query(expression)
        transformed.append(filtered)

    result = save_datasets(transformed, args.output_file, delimiter=delimiter)
    return result


if __name__ == '__main__':
    main()
