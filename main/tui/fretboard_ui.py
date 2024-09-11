


import npyscreen
from typing import List


from lib.guitar import Guitar
from lib.note import Note, NoteInterval
from lib.scale import Scale


class KeySlider(npyscreen.Slider):

	def __init__(self, *args, **kwargs):
		# self.out_of = out_of
		super().__init__(*args, **kwargs)
		
	def translate_value(self):
		# return '123'
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
			self.scale_mode.display()
		
	def create(self):
		y, x = self.useable_space()

		default_mode_number = 0
		default_mode = list(Scale.SCALE_DEFINITIONS.keys())[default_mode_number]
		self.scale_type = self.add(
			npyscreen.TitleSelectOne, 
			scroll_exit=True, 
			exit_left=True, 
			exit_right=True,
			max_height=3, 
			name='Scale Type', 
			value=default_mode_number,
			values=list(Scale.SCALE_DEFINITIONS.keys())
		)

		scale_modes = Scale.SCALE_DEFINITIONS[default_mode]['mode_names']
		self.scale_mode = self.add(
			npyscreen.TitleSelectOne, 
			scroll_exit=True, 
			max_height=10, 
			name='Mode', 
			values=scale_modes,
			# relx=int(x/2),
			# rely=0,
		)

		self.key = self.add(
			TitleKeySlider,
			scroll_exit=True, 
			name='Key',
			label=True,
			out_of=11,
			max_width=50,
		)

class App(npyscreen.NPSAppManaged):
	def onStart(self):
		self.addForm(
			'MAIN', 
			MainForm, 
			name='ASCII Fretboard',
			# minimum_lines=20,
			lines=40,
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