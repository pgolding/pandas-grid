# -*- coding: utf-8 -*-
from . import helpers
from jinja2 import Template
import os
import webbrowser

COLS = ['col-12', 'col-6', 'col-4', 'col-3', 'col-2', 'col-2', 'col-1', 'col-1', 'col-1', 'col-1', 'col-1', 'col-1']

def get_column_css(first_row):
    cols = len(first_row)
    if cols <= 12:
        return COLS[cols-1]
    else:
        return 'col-1'

def render_table(table_data, img_cols=[], filename='grid_output.html', heading='', show=False):
    # compute the cols needed - we can render up to 12 cols
    col_css = get_column_css(table_data[0])

    try:
        #Get the template HTML file that we want to modify
        with open('grid.html', 'r') as f:
            contents = f.read()
        template = Template(contents)
        rendered = template.render(title="This is a test", col_css=col_css, \
                                   img_cols = img_cols, table=table_data, doc_header=heading)
        with open(filename, 'w') as rendered_file:
            rendered_file.writelines(rendered)
        path = os.path.realpath(filename)
        file_url = "file://{}".format(path)
        if show:
            webbrowser.open(file_url, new=1)
        return file_url

    except Exception as e:
        print(e)



#render_table(table_data, [3])
