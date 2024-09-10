
from typing import List

from lib.note import Note, NoteInterval
from lib.scale import Scale

class Guitar:
	
	STANDARD = 'standard'
	TUNING_DEFINITIONS = {
		STANDARD : ['E3', 'A4', 'D4', 'G4', 'B5', 'E5']
	}

	# _tuning = None 
	_max_fret = 24

	# String tuning	
	_string_tunings = None
	_fretboard = None

	def __init__(self, tuning=STANDARD, scale=None):
		assert tuning in Guitar.TUNING_DEFINITIONS.keys()
		self._string_tunings = Guitar.TUNING_DEFINITIONS[tuning]
		self._scale = scale

	@staticmethod 
	def build_empty_fretboard(string_tunings: List[str], max_fret: int) -> List[List[int]]:
		fretboard = []
		for string_tuning in string_tunings:
			fretboard.append([0 for fret in range(0, max_fret)])
		return fretboard
				

	@property
	def fretboard(self, tuning: List[str]):
		if self._fretboard is None:
			self._fretboard = []

		##############################################
		return self._fretboard
	
	@staticmethod
	def tuning_and_scale_to_fretboard_of_degree(string_tunings: List[str], max_fret: int) -> List[List[int]]:
		pass	

	@staticmethod
	def tuning_and_scale_to_fretboard_of_notes(string_tunings: List[str], scale: Scale, max_fret: int) -> List[List[Note]]:
		print(f'sts:{string_tunings}')
		assert sum(scale.interval_recipe) == 12
		fretboard = []
		for string_tuning in string_tunings:
			print(f'st:{string_tuning}')

			string_name = Note.full_name_to_name(string_tuning)

			print('string_name')
			print(string_name)

			# scale_degree_index = None
			# for fret in range(0, max_fret):

			# 	# if string_tuning
			# 	if scale_degree_index is None:
			# 		string_in_scale = scale.note_names.index(string_name)
			# 		print(string_in_scale)
			# 		# exit()
			# 	pass
			
		return fretboard
				



	def print_fretboard(self, note):
		print(note)
		
	
		