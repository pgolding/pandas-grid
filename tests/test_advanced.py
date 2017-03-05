# -*- coding: utf-8 -*-

from .context import griddy

import unittest
import pandas as pd
import os
import uuid

filename = str(uuid.uuid4())[:8] + '.html'
data = ['First col', 'Second col', 'http://placehold.it/100?text="Third col"'] * 3
df = pd.DataFrame(data)
griddy.render_table(df, filename=filename)

class GriddyTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_rendered_html(self):
        self.assertTrue(os.path.isfile(filename))

    def test_css_copied_ok(self):
        self.assertTrue(os.path.isfile('grid.css'))


if __name__ == '__main__':
    unittest.main()
