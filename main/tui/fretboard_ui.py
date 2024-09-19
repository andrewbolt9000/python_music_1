import random
from typing import List

import npyscreen

from lib.guitar import Guitar
from lib.guitar_representation import GUITAR_REPRESENTATIONS, SortedGuitarRepresentationFactory
from lib.note import Note, NoteInterval
from lib.scale import Scale

from monkey_patch import set_text_widths as monkey_patched_set_text_widths
npyscreen.wgtextbox.TextfieldBase.set_text_widths = monkey_patched_set_text_widths


class KeySlider(npyscreen.Slider):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def translate_value(self):
        root_note_name = Note.NOTE_NAMES_2[int(self.value)]
        root_note_name = root_note_name.ljust(2)
        return root_note_name


class TitleKeySlider(npyscreen.wgtitlefield.TitleText):
    _entry_type = KeySlider


class MyGrid(npyscreen.GridColTitles):
    # You need to override custom_print_cell to manipulate how
    # a cell is printed. In this example we change the color of the
    # text depending on the string value of cell.
    def custom_print_cell(self, actual_cell, cell_display_value):


        # Color mapping - maps to theme

        # 'DEFAULT'     : 'WHITE_BLACK',
        # 'FORMDEFAULT' : 'WHITE_BLACK',
        # 'NO_EDIT'     : 'BLUE_BLACK',
        # 'STANDOUT'    : 'CYAN_BLACK',
        # 'CURSOR'      : 'CYAN_BLACK',
        # 'CURSOR_INVERSE': 'BLACK_WHITE',
        # 'LABEL'       : 'CYAN_BLACK',
        # 'LABELBOLD'   : 'BLACK_CYAN',
        # 'CONTROL'     : 'RED_BLACK',
        # 'IMPORTANT'   : 'GREEN_BLACK',
        # 'SAFE'        : 'GREEN_BLACK',
        # 'WARNING'     : 'YELLOW_BLACK',
        # 'DANGER'      : 'RED_BLACK',
        # 'CRITICAL'    : 'BLACK_RED',
        # 'GOOD'        : 'GREEN_BLACK',
        # 'GOODHL'      : 'GREEN_BLACK',
        # 'VERYGOOD'    : 'BLACK_GREEN',
        # 'CAUTION'     : 'YELLOW_BLACK',
        # 'CAUTIONHL'   : 'BLACK_YELLOW',

        color_a = 'DEFAULT' # WHITE
        color_b = 'CURSOR'  # CYAN
        color_c = 'SAFE'    # GREEN
        color_d = 'CAUTION' # YELLOW 
        color_e = 'DANGER'  # RED
        color_string = 'DANGER'
        color_def = 'DEFAULT'

        # Color top row (guide) red
        if type(actual_cell.grid_current_value_index) is tuple \
                and actual_cell.grid_current_value_index[0] == 0:
            actual_cell.color = color_e 
            return
        # Color string names red
        if type(actual_cell.grid_current_value_index) is tuple \
                and actual_cell.grid_current_value_index[1] < 6:
            actual_cell.color = color_e 
            return            

        if cell_display_value == u'◘':
           actual_cell.color = color_a
        elif cell_display_value == 'R':
           actual_cell.color = color_a
        elif cell_display_value == u'●':
           actual_cell.color = color_a
        elif cell_display_value == u'◉':
           actual_cell.color = color_b
        elif cell_display_value == u'⦿':
           actual_cell.color = color_e
        elif cell_display_value == u'◎':
           actual_cell.color = color_d
        elif cell_display_value == u'✪':
           actual_cell.color = color_e

        # Fretboard navigation dots.
        elif cell_display_value == u'.':
           actual_cell.color = color_e

        elif cell_display_value == u'⎔':
           actual_cell.color = color_c

        elif cell_display_value == u'☢︎': # DOESNT WORK
           actual_cell.color = color_b

        # C_SET = u'◘●◉⦿◎✪☢︎⎔▸▶︎►▼◼︎🁢'

        elif cell_display_value == u'🁢':
           actual_cell.color = color_d

        elif cell_display_value == u'◼︎':
           actual_cell.color = color_d

        elif cell_display_value == u'▸':
           actual_cell.color = color_a
        elif cell_display_value in (u'▶︎', u'►', u'▼', u'◼︎', u'🁢'):
            actual_cell.color = color_b
        elif cell_display_value == u'▼':
           actual_cell.color = color_b
        elif cell_display_value == u'►':
           actual_cell.color = color_b
        elif cell_display_value == u'▶︎':
           actual_cell.color = color_b

        # Strings / Frets
        elif cell_display_value == u'|':
           actual_cell.color = color_string
        elif cell_display_value == u'⎯':
           actual_cell.color = color_string
        elif cell_display_value == u'┼':
           actual_cell.color = color_string
        else:
           actual_cell.color = color_b


class MainForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)
    
    def while_editing(self, arg):
        # self.update_fretboard()
        self.representation_sub_style_selector.display()
        self.update_grid_fretboard()

    def adjust_widgets(self):
        if len(self.scale_type.value) > 0:
            scale_type = list(Scale.SCALE_DEFINITIONS.keys())[self.scale_type.value[0]]
            mode_names = Scale.SCALE_DEFINITIONS[scale_type]['mode_names']

            # Set default for mode if not enough options for scale type
            if self.scale_mode.value[0] > len(mode_names) - 1:
                self.scale_mode.value[0] = 0

            self.scale_mode.values = mode_names
            # self.tuning_selector.display()
            self.scale_mode.display()
            self.representation_sub_style_selector.display()

        if len(self.representation_style_selector.value) > 0:
            representation_style = SortedGuitarRepresentationFactory.styles()[self.representation_style_selector.value[0]]
            representation_sub_styles = SortedGuitarRepresentationFactory.sub_styles_for_style(style=representation_style)

            # Set default for mode if not enough options for scale type
            if self.representation_sub_style_selector.value[0] > len(representation_sub_styles) - 1:
                self.representation_sub_style_selector.value[0] = 0

            self.representation_sub_style_selector.values = representation_sub_styles
            self.representation_sub_style_selector.display()
            self.tuning_selector.display()
        
        self.representation_sub_style_selector.display()        
        self.tuning_selector.display()
        self.update_grid_fretboard()

    def update_grid_fretboard(self):
        if len(self.scale_type.value) > 0 \
                and len(self.scale_mode.value) > 0 \
                and len(self.tuning_selector.value) > 0 \
                and len(self.representation_style_selector.value) > 0 \
                and len(self.representation_sub_style_selector.value) > 0:

            representation_style = SortedGuitarRepresentationFactory.styles()[self.representation_style_selector.value[0]]
            representation_sub_style = SortedGuitarRepresentationFactory.sub_styles_for_style(
                style=representation_style
            )[self.representation_sub_style_selector.value[0]]

            tuning_type = list(Guitar.TUNING_DEFINITIONS.keys())[self.tuning_selector.value[0]] 

            scale_type = list(Scale.SCALE_DEFINITIONS.keys())[self.scale_type.value[0]]
            scale_mode_selection = self.scale_mode.value
            scale_key = Note.NOTE_NAMES_2[int(self.scale_key.value)]
            if len(scale_mode_selection) > 0:
                scale_mode = list(Scale.SCALE_DEFINITIONS[scale_type]['mode_names'])[scale_mode_selection[0]]
                scale = Scale(
                    root_name=scale_key,
                    scale_type=scale_type,
                    mode_name=scale_mode,
                ) 
                fretboard = Guitar(scale=scale, tuning=tuning_type)
                representation = SortedGuitarRepresentationFactory.get_representation(style=representation_style, sub_style=representation_sub_style)
                
                # readable_fretboard = fretboard.print_readable_basic(return_string=True, lines_to_list=True, representation=representation)
                readable_fretboard = fretboard.print_readable_basic(
                    return_string=True, 
                    lines_to_list=True, 
                    representation=representation,
                    # representation_style=representation_style,
                    # representation_sub_style=representation_sub_style,
                )

                self.grid_board.values = []
                dim_y = min([self.max_board_size_y, len(readable_fretboard)])
                for y in range(dim_y - 0): # Y
                    row = []
                    dim_x = min([self.max_board_size_x, len(readable_fretboard[y])])
                    for x in range(dim_x - 0): # X
                        row.append(readable_fretboard[y][x])
                    self.grid_board.values.append(row)
                self.tuning_selector.display()    
                self.grid_board.display()
                 
    def create(self):
        y, x = self.useable_space()

        begin_entry_at = 7 #  Label width
        default_scale_mode_value = 0
        default_mode = list(Scale.SCALE_DEFINITIONS.keys())[default_scale_mode_value]
        self.scale_type = self.add(
            npyscreen.TitleSelectOne, 
            scroll_exit=True, 
            exit_left=True, 
            exit_right=True,
            max_height=6, 
            max_width=30,
            name='Type', 
            value=[default_scale_mode_value],
            values=list(Scale.SCALE_DEFINITIONS.keys()),
            begin_entry_at=begin_entry_at,
        )

        scale_modes = Scale.SCALE_DEFINITIONS[default_mode]['mode_names']
        self.scale_mode = self.add(
            npyscreen.TitleSelectOne, 
            scroll_exit=True, 
            max_height=8, 
            max_width=30,
            name='Mode', 
            value=[0],
            values=scale_modes,
            # relx=int(x/2),
            begin_entry_at=begin_entry_at,
            # rely=0,
        )

        self.scale_key = self.add(
            TitleKeySlider,
            scroll_exit=True, 
            name='Key',
            label=True,
            out_of=11,
            max_width=23,
            max_height=3,
            height=4,
            value=9,
            # use_two_lines=True,
            begin_entry_at=begin_entry_at,
        )

        default_rep_style = 0
        representation_styles = SortedGuitarRepresentationFactory.styles()
        representation_sub_styles = SortedGuitarRepresentationFactory.sub_styles_for_style(representation_styles[default_rep_style])

        self.representation_style_selector = self.add(
            npyscreen.TitleSelectOne, 
            # BoxSelectOne, 
            scroll_exit=True, 
            max_height=9, 
            name='Style Category', 
            value=[default_rep_style],
            values=representation_styles, 
            begin_entry_at=begin_entry_at,
            rely=2,
            relx=35,
            max_width=25,
        )

        self.representation_sub_style_selector = self.add(
            npyscreen.TitleSelectOne, 
            # BoxSelectOne, 
            scroll_exit=True, 
            max_height=9,
            name='Sub Style',
            value=[0],
            values=representation_sub_styles,
            begin_entry_at=begin_entry_at,
            rely=11,
            relx=35,
        )

        tuning_types = list(Guitar.TUNING_DEFINITIONS.keys())
        self.tuning_selector = self.add(
            npyscreen.TitleSelectOne, 
            # BoxSelectOne, 
            scroll_exit=True,
            max_height=7,
            name='Tuning',
            value=[0],
            values=tuning_types,
            # relx=int(x/2),
            begin_entry_at=begin_entry_at,
            rely=2,
            relx=68,
            # max_width=40,
        )
        
        self.max_board_size_x = 130
        self.max_board_size_y = 8
        self.grid_board = self.add(
            MyGrid,
            label='Gridboard',
            scroll_exit=True,            
            column_width=1,
            col_margin=0,
            rely=20,
        )

        self.update_grid_fretboard()


class UltraCoolTheme(npyscreen.ThemeManager):
    default_colors = {
    'DEFAULT'     : 'WHITE_BLACK',
    'FORMDEFAULT' : 'WHITE_BLACK',
    'NO_EDIT'     : 'BLUE_BLACK',
    'STANDOUT'    : 'CYAN_BLACK',
    'CURSOR'      : 'CYAN_BLACK',
    'CURSOR_INVERSE': 'BLACK_WHITE',
    'LABEL'       : 'CYAN_BLACK',
    'LABELBOLD'   : 'BLACK_CYAN',
    'CONTROL'     : 'RED_BLACK',
    'IMPORTANT'   : 'GREEN_BLACK',
    'SAFE'        : 'GREEN_BLACK',
    'WARNING'     : 'YELLOW_BLACK',
    'DANGER'      : 'RED_BLACK',
    'CRITICAL'    : 'BLACK_RED',
    'GOOD'        : 'GREEN_BLACK',
    'GOODHL'      : 'GREEN_BLACK',
    'VERYGOOD'    : 'BLACK_GREEN',
    'CAUTION'     : 'YELLOW_BLACK',
    'CAUTIONHL'   : 'BLACK_YELLOW',
}
class DefaultTheme(npyscreen.ThemeManager):
    default_colors = {
    'DEFAULT'     : 'WHITE_BLACK',
    'FORMDEFAULT' : 'WHITE_BLACK',
    'NO_EDIT'     : 'BLUE_BLACK',
    'STANDOUT'    : 'CYAN_BLACK',
    'CURSOR'      : 'WHITE_BLACK',
    'CURSOR_INVERSE': 'BLACK_WHITE',
    'LABEL'       : 'GREEN_BLACK',
    'LABELBOLD'   : 'WHITE_BLACK',
    'CONTROL'     : 'YELLOW_BLACK',
    'IMPORTANT'   : 'GREEN_BLACK',
    'SAFE'        : 'GREEN_BLACK',
    'WARNING'     : 'YELLOW_BLACK',
    'DANGER'      : 'RED_BLACK',
    'CRITICAL'    : 'BLACK_RED',
    'GOOD'        : 'GREEN_BLACK',
    'GOODHL'      : 'GREEN_BLACK',
    'VERYGOOD'    : 'BLACK_GREEN',
    'CAUTION'     : 'YELLOW_BLACK',
    'CAUTIONHL'   : 'BLACK_YELLOW',
}
class App(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(UltraCoolTheme)
        # npyscreen.setTheme(DefaultTheme)
        # npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.addForm(
            'MAIN', 
            MainForm, 
            name='ASCII Guitar Scales',
            # minimum_lines=20,
            # lines=30,
            lines=50,
            minimum_columns=30,
            # columns=120,
            columns=120,
            # max_width=100,
        )

if __name__ == '__main__':
    FretboardApp = App().run()
