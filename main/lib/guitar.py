import math

from typing import List

from lib.note import Note, NoteInterval
from lib.scale import Scale
from lib.guitar_representation import SortedGuitarRepresentationFactory, GuitarRepresentationFactory


class Guitar:
	
	STANDARD = 'Standard'
	DROP_D = 'Drop D'
	A_SPECIAL = 'Andre Special' 
	FRIPP = 'New Standard' 
	BOUZOUKI = 'Bouzouki'
	SEVEN_STR = '7 String'
	TUNING_DEFINITIONS = {
		STANDARD 	: ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
		DROP_D   	: ['D2', 'A2', 'D3', 'G3', 'B3', 'E4'],
		A_SPECIAL  	: ['C2', 'G2', 'D3', 'G3', 'B3', 'E4'],
		SEVEN_STR   : ['B2', 'E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
		FRIPP   	: ['C2', 'G2', 'D3', 'A3', 'E4', 'G4'],
		BOUZOUKI   	: ['D2', 'A2', 'E3', 'B3'],
	}


	# _tuning = None 
	_max_fret = 25

	# String tuning	
	_string_tunings = None
	_fretboard = None

	def __init__(self, tuning=STANDARD, scale=None):
		assert tuning.title() in Guitar.TUNING_DEFINITIONS.keys()
		self._string_tunings = Guitar.TUNING_DEFINITIONS[tuning.title()]
		self._scale = scale
		# self._scaled_filtered_fretboard = Guitar.tuning_and_scale_to_fretboard(
		# 	string_tunings=self._string_tunings,
		# 	scale=self._scale, 
		# 	max_fret=self._max_fret,
		# 	representation=None,
		# 	# representation_type='degree_debug',
		# ) 

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

	# ToDo ? Depenency injected representation of filtered fretboard
	@staticmethod
	def tuning_and_scale_to_fretboard(
		string_tunings: List[str], 
		scale: Scale, 
		max_fret: int,
		representation: None
		# representation_type: str='Full Name Wide', 

	) -> List[List[Note]]:

		# print(f'sts:{string_tunings}')

		# This determins how the string representation will look
		# representation = GuitarRepresentationFactory(representation_type)
		
		# Confirm the interval_recipe is valid
		assert sum(scale.interval_recipe) == 12
		
		# Determine the first root note found on the lowest string
		#  Pass this to the printers so they my highlight chord extensions
		lowest_string_note = Note(full_name=string_tunings[0])
		# Find lowest root not for instrument
		distance_from_lowest_root = Note(name=scale.note_names[0], octave=lowest_string_note.octave) \
		 	+ NoteInterval(semitones=12) \
			- lowest_string_note
		distance_from_lowest_root = distance_from_lowest_root % 12
		lowest_root = lowest_string_note + distance_from_lowest_root

		fretboard = []
		for string_number in range(0, len(string_tunings)):
			string_note = Note(full_name=string_tunings[string_number])
			fretboard.append([])
			for fret in range(0, max_fret):
				fret_note = string_note + NoteInterval(fret)
				if fret_note.name in scale.note_names:
					degree = scale.note_names.index(fret_note.name) + 1
					dist_from_lowest_root = fret_note - lowest_root

					# For the first two octaves above the lowest root, this will be 0
					# 
					double_octave = math.floor(dist_from_lowest_root.semitones / 24)
					single_octave = math.floor(dist_from_lowest_root.semitones / 12)


					# this does not work for 8+ note scales
					# assert len(scale.note_names) == 7, "this does not work for longer scales probably??"
					if (dist_from_lowest_root.semitones // 12) % 2 == 1:
						degree_extension = degree + len(scale.note_names) # this does not work for 8+ note scales
					else:
						# ... == 0
						degree_extension = degree


					# if double_octave % 2 == single_octave % 2:
					# 	degree_extension = degree + len(scale.note_names)
					# else:
					# 	degree_extension = degree

					fretboard[string_number].append(
						representation.found(
							full_name=fret_note.full_name, 
							degree=degree,
							relative_single_octave=single_octave,
							relative_double_octave=double_octave,
							degree_extension=degree_extension,
						)
					)
				else:
					fretboard[string_number].append(
						representation.not_found(full_name=fret_note.full_name)
					)
			
		return fretboard	
				


	# Deprecated??????
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

	def print_readable_basic(
			self, 
			max_fret=None, 
			return_string=True, 
			lines_to_list=False, 
			representation=None,
			top_guide=True,
			dot_guide=True,
	):
		readable_max_fret = max_fret if max_fret is None else self._max_fret
		if representation is None:
			representation = SortedGuitarRepresentationFactory(
				style=representation_style, 
				sub_style=representation_sub_style
			)

		# representation = SortedGuitarRepresentationFactory.get_representation(
		# 	style=representation_style, 
		# 	sub_style=representation_sub_style
		# )		
		scaled_filtered_fretboard = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=self._string_tunings,
			scale=self._scale, 
			max_fret=self._max_fret,
			representation=representation,
		)

		readable = []

		if top_guide:
			# Fret number guide
			readable.append(representation.guide())

		for string_number in reversed(range(0, len(scaled_filtered_fretboard))):
			# Normalize
			scaled_filtered_fretboard[string_number] = [str(e) for e in scaled_filtered_fretboard[string_number]]
			
			readable_line = ''
			human_string_number = Guitar.string_number_human_readable(
				computer_number=string_number,
				total_strings=len(scaled_filtered_fretboard))

			readable_line = readable_line + f'{human_string_number} ({self._string_tunings[string_number]}) '
			readable_line = readable_line + f'{scaled_filtered_fretboard[string_number][0]}|{representation.spacing()}' 
			readable_line = readable_line + representation.spacing().join(scaled_filtered_fretboard[string_number][1:])
			readable_line = readable_line + representation.spacing()

			readable.append(readable_line)

		if dot_guide:
			try:
				# Fret number dot guide
				readable.append(representation.dot_guide())
			except AttributeError:
				# No dot_guide() for this representation.  Just skip.
				pass

		if not lines_to_list:
			readable = '\n'.join(readable)

		if return_string:
			return readable
		else:
			print(readable)

	