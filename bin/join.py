#!/usr/bin/env python
# encoding: utf-8

# pylint: disable=W0141, C0103

import textwrap
import pandas as p
from fn import F
from lib.parse_args import add_common_arguments
from lib.d3_io import load_datasets, save_datasets


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
    parser.add_argument('--on',
                        dest='on',
                        default=None,
                        required=False,
                        nargs='+',
                        help="Common fields to join on")
    parser.add_argument('--left-on',
                        dest='left_on',
                        default=None,
                        required=False,
                        nargs='+',
                        help="Join fields for left side (only two tables allowed)")
    parser.add_argument('--right-on',
                        dest='right_on',
                        default=None,
                        required=False,
                        nargs='+',
                        help="Join fields for right side (only two tables allowed)")
    parser.add_argument('--how',
                        dest='how',
                        default='inner',
                        required=False,
                        choices=('left', 'right', 'outer', 'inner'),
                        help="How to join")

    return parser


def main():
    """@todo: Docstring for main.

    :returns: @todo

    """

    def load_csv(delimiter, filename):
        """@todo: Docstring for load_csv.

        :filename: @todo
        :returns: @todo

        """
        return (type(filename) is file and
                p.read_csv(filename, sep=delimiter)) or \
               (filename.endswith('.gz') and
                p.read_csv(filename, sep=delimiter, compression='gz')) or \
               (filename.endswith('.bz2') and
                p.read_csv(filename, sep=delimiter, compression='bz2')) or \
            p.read_csv(filename, sep=delimiter)

    def merge_data(on, dataset_1, dataset_2, how):
        """@todo: Docstring for merge_data.

        :dataset_1: @todo
        :dataset_2: @todo
        :returns: @todo

        """
        return p.merge(dataset_1, dataset_2, on=on, how=how)

    def normal_join(input_files, on):
        data = map(F(load_datasets, delimiter), input_files)
        transformed = reduce(lambda x, y: merge_data(on, x, y, how), data)

        return transformed

    def mismatched_join(input_files, left_on, right_on, how):
        data = map(F(load_datasets, delimiter), input_files[0:2])
        transformed = p.merge(data[0], data[1],
                              left_on = left_on, right_on = right_on,
                              how=how)
        return transformed


    parser = get_argument_settings()
    args = parser.parse_args()

    input_files = args.input_files
    if len(input_files) < 2:
        print "At least two files are required to join"
        return

    on = args.on
    left_on = args.left_on
    right_on = args.right_on
    delimiter = args.delimiter
    how = args.how

    if on:
        transformed = normal_join(input_files, on, how)
    else:
        transformed = mismatched_join(input_files, left_on, right_on, how)

    # data = map(F(load_datasets, delimiter), input_files)
    # transformed = reduce(lambda x, y: merge_data(on, x, y), data)

    result = save_datasets([transformed], args.output_file,
                           delimiter=delimiter)
    return result


if __name__ == '__main__':
    main()
