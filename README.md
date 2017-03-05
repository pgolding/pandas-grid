## Easy Grid-based HTML Display for Pandas Data Frames ##

I found myself experimenting with data frames that contained text and images, such as one might find in a product catalog. I wanted to try various methods to search the data and then visualize the "search results" including thumbnail images. However, the native methods to view/manipulate HTML inside of a Jupyter Notebook were too visually limited for my liking.

Hence I created Griddy, which is a very simple "helper" function to render a Pandas data frame (up to 12 columns) with a responsive CSS-based grid layout ([Simple Grid](https://github.com/zachacole/Simple-Grid) by Zach Cole). The rendering uses the jinja2 templating library and mark-up.
 
 Installation is easy:
 
 >pip install griddy
 
### How to Use ###
 
Griddy is primarily designed to be used with a Jupyter Notebook, but can also be referenced from any Python program.

```Python
import pandas as pd
import griddy
df = pd.read_csv('csv-data.csv')
griddy.render_table(df)
```

This will create an HTML file 'griddy.html' in the current working directory where the notebook is running. The script will also copy a CSS file 'grid.css' into the working directory. Feel free to edit the CSS file to customize the styling more to your liking.

The full function is:

```Python
render_table(table_data: pd.DataFrame, headings: str =[], filename='griddy.html', \
                 annotation='', show=False, css: str = []):
```

### Parameters ###

#### Filename ####

As you can see, 'griddy.html' is just a default filename. Most likely you will override it with your own more meaningful filename. I tend to automate this when running a set of experiments so that I end up with a succession of HTML files that I can review. 

My preferred pattern is something like: ```lab_experiment_num.html``` where ```lab``` is the name of my current set of experiments and ```experiment``` is the particular experiment with ```num``` representing the iteration - e.g. ```stemming_porter_01.html etc.```

Note that the file name (minus the extension) is used as the ```<title>``` tag for the HTML.

#### headings ####

This enables you to give column headings to the grid:

```Python
headings = ['Text', 'Tags', 'URL']
```

Prepending any of the columng headings with ```<img>``` will cause the renderer to assume that the contents of that column is image URLs and will therefore wrap them with an image tage: ```<img href='contents'>``` tag. 

```Python
headings = ['Text', 'Tags', '<img>URL']
```

Of course, you can style the images using the CSS (e.g. to scale them). I am usually working with PNG thumbnails that are easy to visualize in a table.

#### annotation ####

If this field is present, the first row of the table will contain whatever string is passed into this field. I tend to use this to document a particular experiment.

#### show ####

If set to True, this will cause the resulting HTML file to be opened immediately in a new browser tab (or window).

#### css ####

By default, the script figures out how many columns are in the data frame and adjusts the CSS mark-up for each column element according - see [Simple Grid](http://www.simplegrid.io/). However, you can override with your own values:

```Python
css = ['col-6', 'col-3', 'col-3']
```


 
 
 

