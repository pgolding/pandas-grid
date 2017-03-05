from __future__ import print_function

from jinja2 import Template
import os
import webbrowser
import pandas as pd

# Use pkg_resources to get the correct path name to the locally packaged resources
from pkg_resources import resource_filename
grid_html = resource_filename('griddy', 'resources/grid.html')
grid_css = resource_filename('griddy', 'resources/grid.css')

# Array of column CSS classes indexed by number of columns
# e.g. If table has 4 columns, then return COLS[3] - i.e. 'col-3' as the default col width
COLS = ['col-12', 'col-6', 'col-4', 'col-3', 'col-2', 'col-2', 'col-1', \
        'col-1', 'col-1', 'col-1', 'col-1', 'col-1']

# Helper function to determine default column CSS class
def get_column_styling(num_cols_in_table):
    if num_cols_in_table <= 12:
        return COLS[num_cols_in_table-1]
    else:
        return 'col-1'

def render_table(table_data: pd.DataFrame, headings: str =[], filename='griddy.html', \
                 annotation='', show=False, css: str = []):
    num_of_cols = table_data.shape[1]
    # Make sure there are no more than 12 cols
    if num_of_cols > 12:
        raise ValueError('Too many columns in data frame. Griddy expects 12 or less.')
    # if columns css not given, then calculate a default for all cols
    if not css:
        col_style = get_column_styling(table_data.shape[1])
        css = [col_style] * num_of_cols # Apply same column CSS class to all columns
    # Parse image cols and calculate their index to pass into template renderer
    img_cols=[]
    if headings:
        for i,heading in enumerate(headings):
            if str(heading).startswith('<img>'):
                img_cols.append(i+1) #+1 because Jinja indexes start with 1, not 0
                headings[i] = headings[i].strip('<img>')
    # Now attempt the rendering
    try:
        #Get the local Ninja-fied template HTML file that we want to modify
        with open(grid_html, 'r') as f:
            contents = f.read()
        template = Template(contents)
        rendered = template.render(title=filename.split('.')[0], col_css=css, \
                    img_cols = img_cols, table=table_data.as_matrix(), \
                    headings=headings, doc_header=annotation)
        #Save rendered HTML to current working directory
        with open(filename, 'w') as rendered_file:
            rendered_file.writelines(rendered)
        #And finally put the CSS file in the local directory if it doesn't exist already
        if not os.path.isfile ('grid.css'):
            os.system ("cp {} {}".format(grid_css, 'grid.css'))
        path = os.path.realpath(filename)
        file_url = "file://{}".format(path)
        if show:
            webbrowser.open(file_url, new=1)
        return file_url
    except Exception as e:
        print(e)
        return None
