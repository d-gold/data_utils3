# pylint: disable=W0110

""" Handles getting data in and out of

    TODO:
        Automatic handling of .sql and .hql files
        Support for .json, .csv, dialects, etc
"""

import sys
import re
import csv
import pandas as p
from fn import F


def create_json_reader(orient=None, convert_axes=True,
                       convert_dates=True, keep_default_dates=True,
                       precise_float=False, date_unit=None):
    """@todo: Docstring for create_json_loader.

    :x: @todo
    :returns: @todo

    """
    return lambda x: p.read_json(x,
                                 orient=orient,
                                 convert_axes=convert_axes,
                                 convert_dates=convert_dates,
                                 keep_default_dates=keep_default_dates,
                                 precise_float=precise_float,
                                 date_unit=date_unit)


def create_tsv_reader(compression=None,
                      dialect=None,
                      doublequote=True,
                      escapechar=None,
                      quotechar='"',
                      quoting=csv.QUOTE_MINIMAL,
                      skipinitialspace=False,
                      lineterminator=None,
                      names=None,
                      prefix=None,
                      skiprows=None,
                      skipfooter=None,
                      na_values=None,
                      na_fvalues=None,
                      true_values=None,
                      false_values=None,
                      delimiter=None,
                      usecols=None,
                      delim_whitespace=False,
                      na_filter=True,
                      warn_bad_lines=True,
                      error_bad_lines=False,
                      keep_default_na=True,
                      thousands=None,
                      comment=None,
                      decimal=b'.',
                      parse_dates=False,
                      date_parser=None,
                      nrows=None,
                      infer_datetime_format=False):


    """@todo: Docstring for create_tsv_loader.

    :x: @todo
    :returns: @todo

    """
    return lambda x: p.read_csv(x,
                                sep='\t',
                                compression=compression,
                                dialect=dialect,
                                doublequote=doublequote,
                                escapechar=escapechar,
                                quotechar=quotechar,
                                quoting=quoting,
                                skipinitialspace=skipinitialspace,
                                lineterminator=lineterminator,
                                names=names,
                                prefix=prefix,
                                skiprows=skiprows,
                                skipfooter=skipfooter,
                                na_values=na_values,
                                na_fvalues=na_fvalues,
                                true_values=true_values,
                                false_values=false_values,
                                delimiter=delimiter,
                                usecols=usecols,
                                delim_whitespace=delim_whitespace,
                                na_filter=na_filter,
                                warn_bad_lines=warn_bad_lines,
                                error_bad_lines=error_bad_lines,
                                keep_default_na=keep_default_na,
                                thousands=thousands,
                                comment=comment,
                                decimal=decimal,
                                parse_dates=parse_dates,
                                date_parser=date_parser,
                                nrows=nrows,
                                infer_datetime_format=infer_datetime_format)


def create_csv_reader(compression=None,
                      dialect=None,
                      doublequote=True,
                      escapechar=None,
                      quotechar='"',
                      quoting=csv.QUOTE_MINIMAL,
                      skipinitialspace=False,
                      lineterminator=None,
                      names=None,
                      prefix=None,
                      skiprows=None,
                      skipfooter=None,
                      na_values=None,
                      na_fvalues=None,
                      true_values=None,
                      false_values=None,
                      delimiter=None,
                      usecols=None,
                      delim_whitespace=False,
                      na_filter=True,
                      warn_bad_lines=True,
                      error_bad_lines=False,
                      keep_default_na=True,
                      thousands=None,
                      comment=None,
                      decimal=b'.',
                      parse_dates=False,
                      date_parser=None,
                      nrows=None,
                      infer_datetime_format=False):

    """@todo: Docstring for create_csv_reader.

    :x: @todo
    :returns: @todo

    """
    # Note: comment parameter is not supported.
    return lambda x: p.read_csv(x,
                                sep=',',
                                compression=compression,
                                dialect=dialect,
                                doublequote=doublequote,
                                escapechar=escapechar,
                                quotechar=quotechar,
                                quoting=quoting,
                                skipinitialspace=skipinitialspace,
                                lineterminator=lineterminator,
                                names=names,
                                prefix=prefix,
                                skiprows=skiprows,
                                skipfooter=skipfooter,
                                na_values=na_values,
                                na_fvalues=na_fvalues,
                                true_values=true_values,
                                false_values=false_values,
                                delimiter=delimiter,
                                usecols=usecols,
                                delim_whitespace=delim_whitespace,
                                na_filter=na_filter,
                                warn_bad_lines=warn_bad_lines,
                                error_bad_lines=error_bad_lines,
                                keep_default_na=keep_default_na,
                                thousands=thousands,
                                comment=comment,
                                decimal=decimal,
                                parse_dates=parse_dates,
                                date_parser=date_parser,
                                nrows=nrows,
                                infer_datetime_format=infer_datetime_format)


def create_dsv_reader(sep='\t',
                      compression=None,
                      dialect=None,
                      doublequote=True,
                      escapechar=None,
                      quotechar='"',
                      quoting=csv.QUOTE_MINIMAL,
                      skipinitialspace=False,
                      lineterminator=None,
                      names=None,
                      prefix=None,
                      skiprows=None,
                      skipfooter=None,
                      na_values=None,
                      na_fvalues=None,
                      true_values=None,
                      false_values=None,
                      delimiter=None,
                      usecols=None,
                      delim_whitespace=False,
                      na_filter=True,
                      warn_bad_lines=True,
                      error_bad_lines=False,
                      keep_default_na=True,
                      thousands=None,
                      comment=None,
                      decimal=b'.',
                      parse_dates=False,
                      date_parser=None,
                      nrows=None,
                      infer_datetime_format=False):

    """@todo: Docstring for create_csv_reader.

    :x: @todo
    :returns: @todo

    """
    # Note: comment parameter is not supported.
    return lambda x: p.read_csv(x,
                                sep=sep,
                                compression=compression,
                                dialect=dialect,
                                doublequote=doublequote,
                                escapechar=escapechar,
                                quotechar=quotechar,
                                quoting=quoting,
                                skipinitialspace=skipinitialspace,
                                lineterminator=lineterminator,
                                names=names,
                                prefix=prefix,
                                skiprows=skiprows,
                                skipfooter=skipfooter,
                                na_values=na_values,
                                na_fvalues=na_fvalues,
                                true_values=true_values,
                                false_values=false_values,
                                delimiter=delimiter,
                                usecols=usecols,
                                delim_whitespace=delim_whitespace,
                                na_filter=na_filter,
                                warn_bad_lines=warn_bad_lines,
                                error_bad_lines=error_bad_lines,
                                keep_default_na=keep_default_na,
                                thousands=thousands,
                                comment=comment,
                                decimal=decimal,
                                parse_dates=parse_dates,
                                date_parser=date_parser,
                                nrows=nrows,
                                infer_datetime_format=infer_datetime_format)


def create_excel_reader(sheetname=0,
                        header=0,
                        skiprows=None,
                        skip_footer=0,
                        parse_cols=None,
                        parse_dates=None,
                        date_parser=None,
                        na_values=None,
                        thousands=None,
                        convert_float=True,
                        has_index_names=False):
    """@todo: Docstring for create_excel_reader.

    :x: @todo
    :returns: @todo

    """
    return lambda x: p.read_excel(x,
                                  sheetname=sheetname,
                                  header=header,
                                  skiprows=skiprows,
                                  skip_footer=skip_footer,
                                  parse_cols=parse_cols,
                                  parse_dates=parse_dates,
                                  date_parser=date_parser,
                                  na_values=na_values,
                                  thousands=thousands,
                                  convert_float=convert_float,
                                  has_index_names=has_index_names)


def select_reader(x):
    """@todo: Docstring for select_readerj.

    :x: @todo
    :returns: @todo

    """
    pass


def load_datasets(delimiter, filename):
    """@todo: Docstring for load_csv.

    :filename: @todo
    :returns: @todo

    """

    def load_filename(filename):
        """@todo: Docstring for load_filename.

        :name: @todo
        :returns: @todo

        Note: Loading from filenames allows the result of p.read_csv()
              to be treated as a boolean.
        """
        return (filename.endswith('.gz') and
                p.read_csv(filename, sep=delimiter, compression='gz',
                           encoding='utf-8', warn_bad_lines=False,
                           error_bad_lines=True)) or \
               (filename.endswith('.bz2') and
                p.read_csv(filename, sep=delimiter, compression='bz2',
                           encoding='utf-8', warn_bad_lines=False,
                           error_bad_lines=True)) or \
            p.read_csv(filename, sep=delimiter, encoding='utf-8',
                       warn_bad_lines=False, error_bad_lines=True)

    def load_file_handle(handle):
        """@todo: Docstring for load_file_handle.

        :handle: @todo
        :returns: @todo

        Note: When loading from a file handle, the return value p.read_csv()
              cannot be used as a boolean.
        """

        return p.read_csv(handle, sep=delimiter, encoding='utf-8',
                          warn_bad_lines=False, error_bad_lines=True)

    # TODO: Create a general file loader
    is_handle = type(filename) is file
    if is_handle:   # Loading from sys.stdin does not produce a bool
        return load_file_handle(filename)
    return load_filename(filename)


def create_monkey_writer(underline_header=True,
                         repeat_header_every=25,
                         columns=None,
                         column_widths=None):
    """@todo: Docstring for create_monkey_writer.

    :x: @todo
    :returns: @todo

    """
    pass


def create_tsv_writer(to_clipboard=False):
    """@todo: Docstring for create_tsv_writer.

    :x: @todo
    :returns: @todo

    """
    # return (to_clibpoard and
    #         lambda x: p.to_clipboard()) or \
    #        lambda x: p.to_csv()
    return None


def create_tsv_writer(to_clipboard=False):
    """@todo: Docstring for create_tsv_writer.

    :x: @todo
    :returns: @todo

    """


def create_tsv_writer(to_clipboard=False):
    """@todo: Docstring for create_tsv_writer.

    :x: @todo
    :returns: @todo

    """
    pass


def create_excel_writer():
    """@todo: Docstring for create_excel_writer.

    :arg1: @todo
    :returns: @todo

    """
    pass


def create_json_writer(x):
    """@todo: Docstring for create_json_writer.

    :x: @todo
    :returns: @todo

    """
    pass


def select_writer(x):
    """@todo: Docstring for select_writer.

    :x: @todo
    :returns: @todo

    """
    pass


def save_monkey_readable(dataset, columns=None, column_widths=None):
    """@todo: Docstring for save_monkey_readable.

    :dataset: @todo
    :returns: @todo

    """
    def get_size(name, column, column_widths=None):
        """@todo: Docstring for get_size.

        :column: @todo
        :returns: @todo

        """
        size = (column.dtype == object and column.str.len().max()) or \
            len(str(column.max()))
        full_size = ((len(name) > size) and len(name)) or size
        full_size = (column_widths and
                     name in column_widths and
                     column_widths[name] > full_size and
                     int(column_widths[name])) or full_size
        return full_size

    def format_field(size, field):
        """@todo: Docstring for format_field.

        :size: @todo
        :field: @todo
        :returns: @todo

        """

        formatter = u'{:<' + unicode(int(size)) + u'}'
        str_formatter = u'{:<' + unicode(int(size)) + u'.' + unicode(int(size)) + u'}'
        # print ">>>>", repr(field), repr(size), repr(str_formatter)
        return (type(field) in (str, unicode) and
                str_formatter.format(field)) or \
            formatter.format(field)

    def format_underline(size):
        """@todo: Docstring for format_underline.

        :size: @todo
        :returns: @todo

        """
        return '-' * size

    def format_monkey_row(sizes, row):
        """@todo: Docstring for format_monkey_row.

        :sizes: @todo
        :row: @todo
        :returns: @todo

        """
        data = map(lambda (x, y): unicode(format_field(x, y)), zip(sizes, row))
        return u'  '.join(data)

    if columns:
        dataset = dataset[columns]
    field_sizes = map(lambda x: get_size(x, dataset[x], column_widths), dataset)
    header = format_monkey_row(field_sizes, dataset.columns)
    underline = '  '.join(map(format_underline, field_sizes))
    for i, x in dataset.iterrows():
        if i % 25 == 0:
            if i > 0:
                print
            print header
            print underline
        data = format_monkey_row(field_sizes, x)
        print data.encode('utf-8')
    return True


def save_clipboard(excel=None, sep='\t'):
    """@todo: Docstring for save_clipboard.

    :x: @todo
    :returns: @todo

    """
    return lambda x: p.to_clipboard(excel=excel, sep=sep)


def save_datasets(datasets, outputs, delimiter='\t', use_index=False,
                  monkey_readable=False, columns=None, column_widths=None):
    """@todo: Docstring for save_datasets.

    :datasets: @todo
    :outputs: @todo
    :returns: @todo

    """

    def save_data(dataset, output, delimiter='\t', monkey_readable=False,
                  columns=columns, column_widths=column_widths):
        """@todo: Docstring for save_data.

        :dataset: @todo
        :output: @todo
        :returns: @todo

        """
        return (monkey_readable and save_monkey_readable(dataset,
                                                         columns=columns,
                                                         column_widths=column_widths)) or \
               dataset.to_csv(output, sep=delimiter, index=use_index,
                              encoding='utf-8', cols=columns,
                              column_widths=column_widths)

    outputs = outputs or [sys.stdout]

    # We only want there to be a single output location (either file or
    # stdout), or the same number of files as datasets (inputs)
    ok = len(outputs) == 1 or len(outputs) == len(datasets)

    return (ok and map(lambda x:
                       save_data(x[0], x[1], delimiter,
                                 monkey_readable=monkey_readable,
                                 columns=columns, column_widths=column_widths),
                       zip(datasets, outputs))) \
        or "Error"
