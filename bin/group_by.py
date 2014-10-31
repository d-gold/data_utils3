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
    parser.add_argument('-f', '--fields',
                        dest='fields',
                        default=None,
                        required=True,
                        action='append',
                        help='XXX'
                        'XXX')

    parser.add_argument('--sort',
                        dest='sort',
                        default=True,
                        required=False,
                        action='store_true',
                        help='XXX'
                        'XXX')
    parser.add_argument('--no-sort',
                        dest='sort',
                        required=False,
                        action='store_false',
                        help='XXX'
                        'XXX')

    parser.add_argument('--group-keys',
                        dest='group_keys',
                        default=True,
                        required=False,
                        action='store_true',
                        help='XXX'
                        'XXX')
    parser.add_argument('--no-group-keys',
                        dest='group_keys',
                        required=False,
                        action='store_false',
                        help='XXX'
                        'XXX')

    parser.add_argument('-c', '--count',
                        dest='count',
                        default=False,
                        required=False,
                        action='store_true',
                        help='XXX'
                        'XXX')

    parser.add_argument('--fct', '--apply-function',
                        dest='function',
                        default=None,
                        required=False,
                        choices=['agg', 'aggregate', 'boxplot',
                                 'corr', 'corrwith', 'cov',
                                 'cumcount', 'cummax', 'cummin', 'cumprod',
                                 'cumsum', 'describe', 'diff',
                                 'ffill', 'fillna', 'filter',
                                 'first', 'get_group', 'groups', 'head',
                                 'hist', 'idxmax', 'idxmin', 'irow',
                                 'last', 'mad', 'max', 'mean', 'median',
                                 'min', 'name', 'ngroups', 'nth', 'ohlc',
                                 'pct_change', 'plot', 'prod', 'quantile',
                                 'rank', 'resample', 'shift', 'size',
                                 'skew', 'std', 'sum', 'tail', 'var'],
                        help='XXX'
                        'XXX')

    return parser


def save_grouped_dataset(outputs, group):
    """@todo: Docstring for save_grouped_dataset.

    :outputs: @todo
    :group: @todo
    :returns: @todo

    """
    pass


def main():
    """@todo: Docstring for main.

    :returns: @todo

    """

    def group_data(by, sort, group_keys, dataset):
        """@todo: Docstring for sort_data.

        :columns: @todo
        :ascending: @todo
        :dataset: @todo
        :returns: @todo

        """
        return dataset.groupby(by=by, sort=sort, group_keys=group_keys)

    def apply_function(function, group):
        """@todo: Docstring for apply_functionn.

        :group: @todo
        :function: @todo
        :returns: @todo

        """
        fmap = {'agg': F(group.agg, [np.sum, np.mean, np.std]),
                'aggregate': group.aggregate,
                'boxplot': group.boxplot,
                'corr': group.corr,
                'corrwith': group.corrwith,
                'cov': group.cov,
                'cumcount': group.cumcount,
                'cummax': group.cummax,
                'cummin': group.cummin,
                'cumprod': group.cumprod,
                'cumsum': group.cumsum,
                'describe': group.describe,
                'diff': group.diff,
                'ffill': group.ffill,
                'fillna': group.fillna,
                'filter': group.filter,
                'first': group.first,
                'get_group': group.get_group,
                'groups': group.groups,
                'head': group.head,
                'hist': group.hist,
                'idxmax': group.idxmax,
                'idxmin': group.idxmin,
                'irow': group.irow,
                'last': group.last,
                'mad': group.mad,
                'max': group.max,
                'mean': group.mean,
                'median': group.median,
                'min': group.min,
                'name': group.name,
                'ngroups': group.ngroups,
                'nth': group.nth,
                'ohlc': group.ohlc,
                'pct_change': group.pct_change,
                'plot': group.plot,
                'prod': group.prod,
                'quantile': group.quantile,
                'rank': group.rank,
                'resample': group.resample,
                'shift': group.shift,
                'size': group.size,
                'skew': group.skew,
                'std': group.std,
                'sum': group.sum,
                'tail': group.tail,
                'var': group.var
        }
        return fmap[function]().reset_index()


    parser = get_argument_settings()
    args = parser.parse_args()

    delimiter = args.delimiter
    field_list = flatten_expressions(args.fields, sep=r'\s*[,;]\s*')

    input_files = args.input_files or [sys.stdin]
    data = map(F(load_datasets, delimiter), input_files)

    transformed = map(F(group_data, field_list, args.sort, args.group_keys),
                      data)

    if args.function:
        transformed = map(F(apply_function, args.function), transformed)
        # for x in transformed:
        #     print x
        save_datasets(transformed, args.output_file, delimiter=delimiter)

    else:
        # TODO: This DOES NOT Handle multiple outputs or non-TSV output
        if args.count:
            print u'\t'.join(cons(field_list, ['count']))

        for grouped in transformed:
            for key, group in grouped:
                # TODO: This DOES NOT Handle multiple outputs or non-TSV output
                if args.count:
                    result = u'\t'.join(cons(key, [str(len(group))]))
                    print result.encode('utf-8')
                else:
                    result = save_datasets([group], args.output_file,
                                        delimiter=delimiter)
                    print

    return transformed


if __name__ == '__main__':
    main()

