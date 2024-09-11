


import npyscreen
from typing import List


from lib.guitar import Guitar
from lib.note import Note, NoteInterval
from lib.scale import Scale


class KeySlider(npyscreen.Slider):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
	def translate_value(self):
		root_note_name = Note.NOTE_NAMES_2[int(self.value)]
		root_note_name = root_note_name.rjust(2)
		return root_note_name

class TitleKeySlider(npyscreen.wgtitlefield.TitleText):
	_entry_type = KeySlider


class MainForm(npyscreen.Form):
	def afterEditing(self):
		self.parentApp.setNextForm(None)
	
	def adjust_widgets(self):
		if len(self.scale_type.value) > 0:
			scale_type = list(Scale.SCALE_DEFINITIONS.keys())[self.scale_type.value[0]]
			self.scale_mode.values = Scale.SCALE_DEFINITIONS[scale_type]['mode_names']
			# self.scale_mode.value = 0
			self.scale_mode.display()
		# if self.scale_key.value:
		# 	self.fretboard_viewer.values = ['test']
		if len(self.scale_type.value) > 0 \
				and len(self.scale_mode.value) > 0:
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
				fretboard = Guitar(scale=scale)
				readable_fretboard = fretboard.print_readable_basic(return_string=True, lines_to_list=True, representation_type='color_degree_emoji')
				self.fretboard_viewer.values = readable_fretboard
				self.fretboard_viewer.display()

		# self.update_fretboard()


	def update_fretboard(self):
		if len(self.scale_type.value) > 0 \
				and len(self.scale_mode.value) > 0:
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
				fretboard = Guitar(scale=scale)
				readable_fretboard = fretboard.print_readable_basic(return_string=True, lines_to_list=True, representation_type='color_degree_emoji')
				self.fretboard_viewer.values = readable_fretboard
				self.fretboard_viewer.display()

	def create(self):
		y, x = self.useable_space()


		begin_entry_at = 7 # Label width
		default_mode_number = 0
		default_mode = list(Scale.SCALE_DEFINITIONS.keys())[default_mode_number]
		self.scale_type = self.add(
			npyscreen.TitleSelectOne, 
			scroll_exit=True, 
			exit_left=True, 
			exit_right=True,
			max_height=3, 
			name='Type', 
			value=default_mode_number,
			values=list(Scale.SCALE_DEFINITIONS.keys()),
			begin_entry_at=begin_entry_at,
		)

		scale_modes = Scale.SCALE_DEFINITIONS[default_mode]['mode_names']
		self.scale_mode = self.add(
			npyscreen.TitleSelectOne, 
			scroll_exit=True, 
			max_height=10, 
			name='Mode', 
			value=5,
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
			max_width=50,
			height=4,
			value=9,
			begin_entry_at=begin_entry_at,
		)

		self.fretboard_viewer = self.add(
			npyscreen.TitlePager,
			scroll_exit=True, 
			name='Fretboard',
			label=True,
			max_width=75,		
			values=[],
		)
		# self.update_fretboard()

class App(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm(
			'MAIN', 
			MainForm, 
			name='ASCII Fretboard',
			# minimum_lines=20,
			lines=25,
		)

if __name__ == '__main__':
	FretboardApp = App().run()












		# self.myName        = self.add(npyscreen.TitleText, name='Name')
		# self.myDepartment  = self.add(npyscreen.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
		# self.myDate        = self.add(npyscreen.TitleDateCombo, name='Date Employed')
		# self.add(npyscreen.TitleDateCombo, name="Date:", max_width=x // 2)
		# self.add(npyscreen.TitleMultiSelect, relx=x // 2 + 1, rely=2, value=[1, 2], name="Pick Several", values=["Option1", "Option2", "Option3"], scroll_exit=True)
		# You can use the negative coordinates
		# self.add(npyscreen.TitleFilename, name="Filename:", rely=-5)


# #!/usr/bin/env python3
# import npyscreen

# class App(npyscreen.StandardApp):
#     def onStart(self):
#         self.addForm("MAIN", MainForm, name="Hello Medium!")

# class MainForm(npyscreen.FormBaseNew):
#     def create(self):
#         # Get the space used by the form

# MyApp = App()
# MyApp.run()