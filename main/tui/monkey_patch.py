#!/usr/bin/python
# import curses
# import curses.ascii
# import sys
# import locale

# This monkey patch allows grids to be used with column_width=1.  
#  Otherwise the library breaks for that config.
def set_text_widths(self):
    if self.on_last_line:
        self.maximum_string_length = self.width - 0  # Leave room for the cursor
    else:   
        self.maximum_string_length = self.width - 0  # Leave room for the cursor at the end of the string.

