import json
import random
from typing import List

import npyscreen

from lib.guitar import Guitar
from lib.guitar_representation import SortedGuitarRepresentationFactory
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
        elif cell_display_value == u'▼':
           actual_cell.color = color_e
        elif cell_display_value == u'►':
           actual_cell.color = color_b
        elif cell_display_value == u'▶︎':
           actual_cell.color = color_b
        # elif cell_display_value in (u'▶︎', u'►', u'▼', u'◼︎', u'🁢'):
        #     actual_cell.color = color_b

        # Strings / Frets
        elif cell_display_value == u'|':
           actual_cell.color = color_string
        elif cell_display_value == u'⎯':
           actual_cell.color = color_string
        elif cell_display_value == u'┼':
           actual_cell.color = color_string
        else:
           actual_cell.color = color_b

class SavedForm(npyscreen.Popup):
    def create(self):
        y, x = self.useable_space()
        self.shortcut_text = self.add(
            npyscreen.FixedText,
            value='CONFIGURATION SAVED',
            relx=x-27,
            rely=y-4,
        )    

    def on_ok(self):
        self.parentApp.switchForm('MAIN')

    def afterEditing(self):
        # self.save_user_settings()
        self.parentApp.switchForm('MAIN')



class MainForm(npyscreen.Form):
    user_settings_path = './user_settings.json'
    DEFAULT_SAVE_INSTRUCTIONS = '^S to save configuration'
    DEFAULT_EXIT_INSTRUCTIONS = '^C to exit'


    # def on_cancel(self):
        # self.parentApp.switchForm(None)

    # def on_ok(self):
        # Exit the application if the OK button is pressed.
        # self.parent.parentApp.switchForm(None)
        # self.parentApp.switchForm(None)

    def save_user_settings(self, *args, **kwargs): 
        with open(self.user_settings_path, 'w') as file:
            new_user_settings = {
                'scale_type':  self.scale_type.value[0],
                'scale_mode':  self.scale_mode.value[0],
                'scale_key':  self.scale_key.value,
                'representation_style_selector':  self.representation_style_selector.value[0],
                'representation_sub_style_selector':  self.representation_sub_style_selector.value[0],
                'tuning_selector':  self.tuning_selector.value[0],
            }
            json_string = json.dumps(new_user_settings, default=lambda o: o.__dict__, sort_keys=True, indent=2)
            file.write(json_string)    
        self.shortcut_text.value = '      SAVED'
        self.shortcut_text.display()
        self.parentApp.switchForm('SAVED')


    def afterEditing(self):
        self.save_user_settings()
        self.parentApp.switchForm('SAVED')

    def while_editing(self, arg):
        # self.update_fretboard()
        self.representation_sub_style_selector.display()
        # self.update_grid_fretboard()

    def adjust_widgets(self):
        # self.parentApp.switchForm(None)
        # exit()
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
        self.shortcut_text.value = self.DEFAULT_SAVE_INSTRUCTIONS


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

                self.shortcut_text.display()
                self.exit_text.display()

    def create(self):
        # Load settings
        try:
            with open(self.user_settings_path, 'r') as file:
                # json_string = file.read()
                user_settings = json.load(file)
                self.user_settings = user_settings
                # self.user_settings = None
        except FileNotFoundError:
            # Defaults
            self.user_settings = {
                'scale_type':  0,
                'scale_mode':  0,
                'scale_key':  9, # A
                'representation_style_selector':  0,
                'representation_sub_style_selector':  0,
                'tuning_selector':  0,
            }

        y, x = self.useable_space()

        begin_entry_at = 7 #  Label width

        default_mode = list(Scale.SCALE_DEFINITIONS.keys())[self.user_settings['scale_mode']]
        self.scale_type = self.add(
            npyscreen.TitleSelectOne, 
            scroll_exit=True, 
            exit_left=True, 
            exit_right=True,
            max_height=6, 
            max_width=30,
            name='Type', 
            value=[self.user_settings['scale_type']],
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
            value=[self.user_settings['scale_mode']],
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
            value=self.user_settings['scale_key'],
            # use_two_lines=True,
            begin_entry_at=begin_entry_at,
        )

        representation_styles = SortedGuitarRepresentationFactory.styles()
        representation_sub_styles = SortedGuitarRepresentationFactory.sub_styles_for_style(
            representation_styles[
                self.user_settings['representation_sub_style_selector']
            ]
        )

        self.representation_style_selector = self.add(
            npyscreen.TitleSelectOne, 
            # BoxSelectOne, 
            scroll_exit=True, 
            max_height=9, 
            name='Style Category', 
            value=[self.user_settings['representation_style_selector']],
            values=representation_styles, 
            begin_entry_at=begin_entry_at,
            rely=2,
            relx=33,
            max_width=25,
        )

        self.representation_sub_style_selector = self.add(
            npyscreen.TitleSelectOne, 
            # BoxSelectOne, 
            scroll_exit=True, 
            max_height=9,
            name='Sub Style',
            value=[self.user_settings['representation_sub_style_selector']],
            values=representation_sub_styles,
            begin_entry_at=begin_entry_at,
            rely=11,
            relx=33,
        )

        tuning_types = list(Guitar.TUNING_DEFINITIONS.keys())
        self.tuning_selector = self.add(
            npyscreen.TitleSelectOne, 
            # BoxSelectOne, 
            scroll_exit=True,
            max_height=7,
            name='Tuning',
            value=[self.user_settings['tuning_selector']],
            values=tuning_types,
            begin_entry_at=begin_entry_at,
            rely=2,
            relx=60,
        )
        
        self.max_board_size_x = 130
        self.max_board_size_y = 8
        self.grid_board = self.add(
            MyGrid,
            label='Gridboard',
            scroll_exit=True,            
            exit_left=True, 
            exit_right=True,            
            exit_top=True,
            exit_bottom=True,
            column_width=1,
            col_margin=0,
            rely=20,
        )

        self.shortcut_text = self.add(
            npyscreen.FixedText,
            value=self.DEFAULT_SAVE_INSTRUCTIONS,
            relx=x-27,
            rely=y-5,
        )
        self.exit_text = self.add(
            npyscreen.FixedText,
            value=self.DEFAULT_EXIT_INSTRUCTIONS,
            relx=x-27,
            rely=y-4,
        )
        self.update_grid_fretboard()

        self.add_handlers({"^S": self.save_user_settings})



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
        form = self.addForm(
            'MAIN', 
            MainForm, 
            name='Fretboard Computer',
            # minimum_lines=20,
            lines=46,
            max_lines=50,
            minimum_columns=25,
            # columns=120,
            max_columns=160,
            # max_width=100,
        )
        save_form = self.addForm(
            'SAVED',
            SavedForm,
            lines=46,
            max_lines=50,
            minimum_columns=30,
            # columns=120,
            max_columns=160,            
        )


if __name__ == '__main__':
    FretboardApp = App().run()
