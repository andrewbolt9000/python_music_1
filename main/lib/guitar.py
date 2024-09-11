
from typing import List

from lib.note import Note, NoteInterval
from lib.scale import Scale


class NoteRepresentation:
	def found(self, full_name, degree=None):
		return Note(full_name=full_name)

	def not_found(self, full_name=None, degree=None):
		return None 

	def spacing(self, full_name=None, degree=None):
		return '-'


class FullNameRepresentation:
	def found(self, full_name, degree=None):
		return full_name

	def not_found(self, full_name=None, degree=None):
		return 0

	def spacing(self, full_name=None, degree=None):
		return '-'


class BasicNameRepresentation:
	def found(self, full_name, degree=None):
		return Note.full_name_to_name(full_name=full_name)

	def not_found(self, full_name=None, degree=None):
		return None

	def spacing(self, full_name=None, degree=None):
		return '-'



class NamelessRepresentation:
	def found(self, full_name, degree=None):
		return 'O'

	def not_found(self, full_name=None, degree=None):
		return '+'

	def spacing(self, full_name=None, degree=None):
		return '-'


class EmojiRepresentation:
	def found(self, full_name, degree=None):
		return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ScaleDegreeRepresentation:
	def found(self, full_name, degree=None):
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return '+'

	def spacing(self, full_name=None, degree=None):
		return '-'


class DegreeEmojiRepresentation:
	def found(self, full_name, degree=None):
		if degree == 0:
			return '◉'
		elif degree == 3:
			return '◎'
		elif degree == 5:
			return '⦿'
		else:
			return '●'

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'


class ColorDegreeEmojiRepresentation:
	def found(self, full_name, degree=None):
		if degree == 0:
			return '●'
		# elif degree == 3:
		# 	return '🟢'
		# elif degree == 5:
		# 	return '🟢'
		else:
			return '⦿'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'




def GuitarRepresentationFactory(representation_type):
	representations = {
		"note_object": NoteRepresentation,
		"full_name": FullNameRepresentation,
		"basic_name": BasicNameRepresentation,
		"nameless": NamelessRepresentation,
		"emoji": EmojiRepresentation,
		"degree": ScaleDegreeRepresentation,
		"degree_emoji": DegreeEmojiRepresentation,
		"color_degree_emoji": ColorDegreeEmojiRepresentation,
	}
	return representations[representation_type]()

class Guitar:
	
	STANDARD = 'standard'
	TUNING_DEFINITIONS = {
		STANDARD : ['E3', 'A4', 'D4', 'G4', 'B5', 'E5']
	}


	# _tuning = None 
	_max_fret = 25

	# String tuning	
	_string_tunings = None
	_fretboard = None

	def __init__(self, tuning=STANDARD, scale=None):
		assert tuning in Guitar.TUNING_DEFINITIONS.keys()
		self._string_tunings = Guitar.TUNING_DEFINITIONS[tuning]
		self._scale = scale

		self._scaled_filtered_fretboard = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=self._string_tunings,
			scale=self._scale, 
			max_fret=self._max_fret,
			representation_type='note_object',
		) 


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
	def tuning_to_fretboard_of_all_notes(string_tunings: List[str], max_fret: int) -> List[List[Note]]:
		# print(f'sts:{string_tunings}')
		fretboard = []
		for string_number in range(0, len(string_tunings)):
			string_note = Note(full_name=string_tunings[string_number])
			fretboard.append([])
			for fret in range(0, max_fret):
				fret_note = string_note + NoteInterval(fret)
				fretboard[string_number].append(fret_note)
			
		return fretboard		


	# Depenency injected representation of filtered fretboard
	@staticmethod
	def tuning_and_scale_to_fretboard(
		string_tunings: List[str], 
		scale: Scale, 
		max_fret: int,
		representation_type: str='full_name', 

	) -> List[List[Note]]:
		# print(f'sts:{string_tunings}')
		representation = GuitarRepresentationFactory(representation_type)
		assert sum(scale.interval_recipe) == 12
		fretboard = []
		for string_number in range(0, len(string_tunings)):
			string_note = Note(full_name=string_tunings[string_number])
			fretboard.append([])
			for fret in range(0, max_fret):
				fret_note = string_note + NoteInterval(fret)
				if fret_note.name in scale.note_names:
					degree = scale.note_names.index(fret_note.name)
					fretboard[string_number].append(representation.found(full_name=fret_note.full_name, degree=degree))
				else:
					fretboard[string_number].append(representation.not_found(full_name=fret_note.full_name))
			
		return fretboard	
				



	@staticmethod
	def tuning_and_scale_to_fretboard_of_notes(string_tunings: List[str], scale: Scale, max_fret: int) -> List[List[Note]]:
		# print(f'sts:{string_tunings}')
		assert sum(scale.interval_recipe) == 12
		fretboard = []
		for string_number in range(0, len(string_tunings)):
			string_note = Note(full_name=string_tunings[string_number])
			fretboard.append([])
			for fret in range(0, max_fret):
				fret_note = string_note + NoteInterval(fret)
				if fret_note.name in scale.note_names:
					fretboard[string_number].append(fret_note)
				else:
					fretboard[string_number].append(None)
			
		return fretboard	
				

	@staticmethod
	def tuning_and_scale_to_fretboard_of_notes_OLD(string_tunings: List[str], scale: Scale, max_fret: int) -> List[List[Note]]:
		# print(f'sts:{string_tunings}')
		assert sum(scale.interval_recipe) == 12
		fretboard = []
		for string_tuning in string_tunings:
			print(f'st:{string_tuning}')

			string_name = Note.full_name_to_name(string_tuning)

			print('string_name')
			print(string_name)

			scale_degree_index = None
			for fret in range(0, max_fret):
				fret_note = Note()
				if fret == 0:
					pass 


				# if string_tuning
				if scale_degree_index is None:
					# No reference point to scale
					string_in_scale = scale.note_names.index(string_name)
					print(f'found string {string_in_scale}')
					scale_degree_index = scale.note_nam
					# exit()
				else:
					pass
			
		return fretboard
				
	@staticmethod
	def string_number_human_readable(computer_number: int, total_strings: int=6):
		return total_strings - computer_number

	def print_readable_basic(self, return_string=False, lines_to_list=False, representation_type='emoji'):
		representation = GuitarRepresentationFactory(representation_type)
		scaled_filtered_fretboard = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=self._string_tunings,
			scale=self._scale, 
			max_fret=self._max_fret,
			representation_type=representation_type,
		)

		readable = []

		# Fret number guide
		guide_line = f'String    {representation.spacing()}|     3   5   7   9     12    15  17  19  21    24'
		readable.append(guide_line)

		for string_number in reversed(range(0, len(scaled_filtered_fretboard))):
			readable_line = ''
			human_string_number = Guitar.string_number_human_readable(
				computer_number=string_number,
				total_strings=len(scaled_filtered_fretboard))
			readable_line = readable_line + f'{human_string_number} - ({self._string_tunings[string_number]})  '
			readable_line = readable_line + f'{scaled_filtered_fretboard[string_number][0]}|-' 
			readable_line = readable_line + representation.spacing().join(scaled_filtered_fretboard[string_number][1:])
			readable.append(readable_line)

		if not lines_to_list:
			readable = '\n'.join(readable)

		if return_string:
			return readable
		else:
			print(readable)

	def print_fretboard(self, note):
		print(note)
		
	
		