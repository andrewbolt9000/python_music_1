import math

from typing import List

from lib.note import Note, NoteInterval
from lib.scale import Scale
from lib.guitar_representation import SortedGuitarRepresentationFactory


class Guitar:
	
	STANDARD = 'Standard'
	DROP_D = 'Drop D'
	A_SPECIAL = 'Andre Special' 
	FRIPP = 'New Standard' 
	BOUZOUKI = 'Bouzouki'
	BASS_GUITAR = 'Bass'
	SEVEN_STR = '7 String'
	TUNING_DEFINITIONS = {
		STANDARD 	: ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
		DROP_D   	: ['D2', 'A2', 'D3', 'G3', 'B3', 'E4'],
		A_SPECIAL  	: ['C2', 'G2', 'D3', 'G3', 'B3', 'E4'],
		SEVEN_STR   : ['B2', 'E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
		FRIPP   	: ['C2', 'G2', 'D3', 'A3', 'E4', 'G4'],
		BOUZOUKI   	: ['D2', 'A2', 'E3', 'B3'],
		BASS_GUITAR : ['E1', 'A1', 'D2', 'G2'],
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

	@staticmethod 
	def build_empty_fretboard(string_tunings: List[str], max_fret: int) -> List[List[int]]:
		fretboard = []
		for string_tuning in string_tunings:
			fretboard.append([0 for fret in range(0, max_fret)])
		return fretboard

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
		representation: str,
	) -> List[List[Note]]:

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
						degree_extension_octave_up = degree
					else:
						# ... == 0
						degree_extension = degree
						degree_extension_octave_up = degree + len(scale.note_names)

					fretboard[string_number].append(
						representation.found(
							full_name=fret_note.full_name, 
							degree=degree,
							relative_single_octave=single_octave,
							relative_double_octave=double_octave,
							degree_extension=degree_extension,
							degree_extension_octave_up=degree_extension_octave_up,
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



class GuitarStringException(Exception):
    def __init__(self, message, errors=None):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
          

class GuitarString:
	note = None 
	human_number = None

	def __init__(self, note, human_number):
		self.note = note 
		self.human_number = human_number

	def __repr__(self):
		return f'<GuitarString note:{self.note.full_name}  human_number:{self.human_number}>'

class GuitarNoteException(Exception):
    def __init__(self, message, errors=None):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
          

class GuitarNote(Note):
	_note = None 
	_fret = None

	# Represents literal wire strings of a guitar (not char strings)
	_guitar_string_number = None 
	_guitar_string_name = None 

	def __init__(self, guitar, note=None, *args, **kwargs):
		self._guitar = guitar 
		# ??? Nessessary for debug?  Inheritance should be fine
		self._note = note 
		if note is None:
			super().__init__(*args, **kwargs)
		else:
			super().__init__(full_name=note.full_name)

	@property
	def fret(self):
		if self._fret is None:
			result = GuitarNote.fret_or_string_to_note()
		elif self._guitar_string is None:
			pass 
		elif self._fret is None and self._guitar_string is None:
			# Select first one we can find (for now)
			GuitarNote.all_fretboard_locations_for_note(note=self._note, guitar=self._guitar)
		return self._fret
	
	@property
	def guitar_string_name(self):
		if self._guitar_string_name is None:
			pass
			# result = GuitarNote.fret_or_string_to_note()

		return self._guitar_string_name


	@property
	def _guitar_string_number(self):
		if self._guitar_string_number is None:
			pass
			# result = GuitarNote.fret_or_string_to_note()
		return self._guitar_string_number


	@staticmethod
	def all_fretboard_locations_for_note(note, guitar):
		locations = []

		guitar_strings = []
		for i_string_tunings, string_name in enumerate(guitar._string_tunings):
			guitar_strings.append(
				GuitarString(
					note=Note(full_name=string_name), 
					human_number=Guitar.string_number_human_readable(
						computer_number=i_string_tunings,
						total_strings=len(guitar._string_tunings)
					)
				)
			)

		# print(guitar_strings)
		print('================')

		for guitar_string in guitar_strings:

			difference = note - guitar_string.note
			print(note)
			print(guitar_string.note)
			print(difference.semitones)
			print('----------')
			# difference = guitar_string.note - note
			if difference.semitones >= 0:
				locations.append(dict(guitar_string=guitar_string, fret=difference.semitones))
		return locations








