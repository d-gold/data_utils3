# pylint: disable=W0110, W0622

import sys
import argparse
from fn import F
# from toolz.functoolz import curry, juxt
from toolz.functoolz import juxt


def add_common_arguments(overrides=None, description=None, epilog=None):
    """@todo: Docstring for add_common_arguments.

    :overrides: @todo
    :description: @todo
    :epilog: @todo

    :returns: @todo

    """
    if not overrides:
        overrides = []

    parser = argparse.ArgumentParser(
        description=description, epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    args = (
    #     # Input
        ('i', F(parser.add_argument,
                '-i', '--input',
                metavar="FILE",
                nargs='+',
                type=str,
                default=None,
                dest='input_files',
                help='The CSV file to operate on. If omitted, will accept '
                'input on STDIN.')),
        ('o', F(parser.add_argument,
                '-o', '--output',
                metavar="FILE",
                type=file,
                default=None,
                dest='output_file',
                help='The file to write the results to If omitted, this '
                'default to STDOUT..')),
        ('if', F(parser.add_argument,
                 '--if', '--input-format',
                 metavar="FORMAT",
                 choices=['auto', 'tsv', 'csv', 'json'],
                 default='auto',
                 required=False,
                 type=str,
                 dest='input_format',
                 help='XXX ..')),
        ('of', F(parser.add_argument,
                 '--of', '--output-format',
                 metavar="FORMAT",
                 choices=['auto', 'monkey', 'tsv', 'csv', 'json'],
                 default='auto',
                 required=False,
                 type=str,
                 dest='output_format',
                 help='XXX ..')),

    #     ('b', curry(parser.add_argument, '-b', '--doublequote',
    #                 dest='doublequote', action='store_true',
    #                 help='Whether or not double quotes are doubled in the '
    #                 'input CSV file.')),
    #     ('B', curry(parser.add_argument, '-B', '--ignore-blank-lines',
    #                 dest='ignore_blank_lines', action='store_true',
    #                 help='Ignore blank lines in the CSV file.')),
    #     ('c', curry(parser.add_argument, '-c', '--comment-regex',
    #                 dest='comment_regex', default='^\\s*#',
    #                 help='Specify a regex to indicate comment rows')),
    #     ('C', curry(parser.add_argument, '-C', '--add-comments',
    #                 dest='add_comments', action='store_true',
    #                 help='Add commented sections to output')),
        ('d', F(parser.add_argument,
                '-d', '--delimiter',
                dest='delimiter',
                default='\t',
                help='Delimiting character of the input CSV file.')),
    #     ('e', curry(parser.add_argument, '-e', '--encoding', dest='encoding',
    #                 default='utf-8',
    #                 help='Specify the encoding the input CSV file.')),
    #     ('H', curry(parser.add_argument, '-H', '--no-header-row',
    #                 dest='no_header_row', action='store_true',
    #                 help='Specifies that the input CSV file has no header '
    #                 'row. Will create default headers.')),
    #     ('l', curry(parser.add_argument, '-l', '--linenumbers',
    #                 dest='line_numbers', action='store_true',
    #                 help='Insert a column of line numbers at the front of the '
    #                 'output. Useful when piping to grep or as a simple '
    #                 'primary key.')),
    #     ('p', curry(parser.add_argument, '-p', '--escapechar',
    #                 dest='escapechar',
    #                 help='Character used to escape the delimiter if '
    #                 '--quoting 3 ("Quote None") is specified and to escape '
    #                 'the QUOTECHAR if --doublequote is not specified.')),
    #     ('q', curry(parser.add_argument, '-q', '--quotechar', dest='quotechar',
    #                 help='Character used to quote strings in the input CSV '
    #                 'file.')),
    #     ('S', curry(parser.add_argument, '-S', '--skipinitialspace',
    #                 dest='skipinitialspace', default=False,
    #                 action='store_true',
    #                 help='Ignore whitespace immediately following the '
    #                 'delimiter.')),
    #     ('t', curry(parser.add_argument, '-t', '--tabs', dest='tabs',
    #                 action='store_true',
    #                 help='Specifies that the input CSV file is delimited with '
    #                 'tabs. Overrides "-d".')),
    #     ('u', curry(parser.add_argument, '-u', '--quoting', dest='quoting',
    #                 type=int, choices=[0, 1, 2, 3],
    #                 help='Quoting style used in the input CSV file. 0 = Quote '
    #                 'Minimal, 1 = Quote All, 2 = Quote Non-numeric, 3 = '
    #                 'Quote None.')),
    #     ('v', curry(parser.add_argument, '-v', '--verbose', dest='verbose',
    #                 action='store_true',
    #                 help='Print detailed tracebacks when errors occur.')),
    #     ('z', curry(parser.add_argument, '-z', '--maxfieldsize',
    #                 dest='maxfieldsize', type=int,
    #                 help='Maximum length of a single field in the input '
    #                 'CSV file.')),
    #     ('strip-comments', curry(parser.add_argument, '--strip-comments',
    #                              dest='strip_comments', action='store_true',
    #                              help='Strip comments from input')),
    #     ('zero', curry(parser.add_argument, '--zero', dest='zero_based',
    #                    action='store_true',
    #                    help='When interpreting or displaying column numbers, '
    #                    'use zero-based numbering instead of the default '
    #                    '1-based numbering.')))
    )

    # TODO:
    # Add parser sections for csv, tsv, json in and outs. Make sure these
    # filter correctly
    # input_general = parser.add_argument_group(title='Input options',
    #                                            description='General input options')
    # output_general = parser.add_argument_group(title='Output options',
    #                                            description='Output options')
    # output_general.add_argument('--oc', '--output-columns',
    #                             metavar='COLUMNS',
    #                             nargs='+',
    #                             type=str,
    #                             default=None ,
    #                             dest='output_columns',
    #                             help='Select the columns and their order to output')

    # csv_in = parser.add_argument_group(title='CSV and TSV input options',
    #                                    description='Delimited...')
    # csv_in.add_argument('--id', '--input-delimiter',
    #                     dest='input_delimiter',
    #                     default='\t',
    #                     required=False,
    #                     type=str,
    #                     help='Delimiter for ...')
    # csv_out = parser.add_argument_group(title='CSV and TSV output options',
    #                                     description='Delimited...')
    # csv_out.add_argument('--od', '--output-delimiter',
    #                     dest='output_delimiter',
    #                     default='\t',
    #                     required=False,
    #                     type=str,
    #                     help='Delimiter for ...')
    # json_in = parser.add_argument_group(title='JSON output options',
    #                                     description='Delimited...')
    # json_out = parser.add_argument_group(title='JSON output options',
    #                                      description='Delimited...')
    # monkey_out = parser.add_argument_group(title='Monkey-Readble output',
    #                                    description='Monkey -Radble output')
    # monkey_out.add_argument('--cw', '--column_widths',
    #                         metavar='COLUMN_WIDTHS',
    #                         nargs='+',
    #                         type=str,
    #                         default=None ,
    #                         dest='column_widths',
    #                         help='Specify a maximum width for columns.')

    functions = filter(lambda (override_option, f):
                       override_option not in overrides,
                       args)
    functions = map(lambda(override_option, f): f, functions)
    _ = tuple(juxt(functions)())

    return parser
