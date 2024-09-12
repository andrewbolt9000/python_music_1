
from typing import List

from lib.note import Note, NoteInterval
from lib.scale import Scale



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f'{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}')
# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)


class RepresentationInterface:
	def found(self, full_name, degree=None):
		return None

	def not_found(self, full_name=None, degree=None):
		return None

	def spacing(self, full_name=None, degree=None):
		return None

	def guide(self):
		# default_guide = f'String  |_|_|_3_|_5_|_7_|_9_|_|_12|_|_15|_17|_19|_21|_|_24'		
		# default_guide = f'String  | | | 3 | 5 | 7 | 9 | | 12| | 15| 17| 19| 21| | 24'		
		default_guide = f'String        3   5   7   9     12    15  17  19  21    24'		
		return default_guide


class NoteRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return Note(full_name=full_name)

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	
	def guide(self):
		return f' String  ||      {bcolors.OKCYAN}3      5      7      9       12     15   17   19   21     24{bcolors.ENDC}'		


class FullNameRepresentationV2(RepresentationInterface):
	def found(self, full_name, degree=None):
		return full_name.rjust(3, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	
	def guide(self):
		return f' String  ||            3       5       7       9          12          15      17      19      21          24'		


class FullNameRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return full_name

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'

	def guide(self):
		return f' String  |     3    5    7    9      12     15   17   19   21     24'		


class BasicNameRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return Note.full_name_to_name(full_name=full_name).rjust(2, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String  ||       3     5     7     9       12       15    17    19    21       24'		
	


class BasicNameRepresentationWide(RepresentationInterface):
	def found(self, full_name, degree=None):
		return Note.full_name_to_name(full_name=full_name).rjust(3, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String  ||           3       5       7       9          12          15      17      19      21          24'		
	


class NamelessRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return 'O'

	def not_found(self, full_name=None, degree=None):
		return '+'

	def spacing(self, full_name=None, degree=None):
		return '-'


class EmojiRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ScaleDegreeRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'
	def guide(self):
		return f'String        3   5   7   9    12    15  17  19  21    24'


class ScaleDegreeAltRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	def guide(self):
		return f'String        3   5   7   9     12    15  17  19  21    24'


class ScaleDegreeRepresentationWide(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			d = '●'
		else:
			d = degree

		return f'{d}'.rjust(3, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String  ||           3       5       7       9          12          15      17      19      21          24'		



class ScaleDegreeNoStringsRepresentationWide(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			d = '●'
		else:
			d = degree

		return ' ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self):
		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		


class DotsNoStringsRepresentationWide(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			d = '◎'
		else:
			d = '●'

		return ' ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self):
		return f' String 0    1       3       5       7       9          12          15      17      19      21          24'		



class BasicNoStringsRepresentationWide(RepresentationInterface):
	def found(self, full_name, degree=None):
		
		name = Note.full_name_to_name(full_name=full_name)
		if degree == 1:
			return '●' + f'{name}'.ljust(2, ' ')
		else:
			return ' ' + f'{name}'.ljust(2, ' ')
		# if degree == 1:
		# 	d = '●'
		# else:
		# 	d = degree

		return ' ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self):
		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		



class CleanRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '●'
			# return '⦿'
			# return '◎'
		# return '●'
		# return '⦿'
		return '◎'
	def not_found(self, full_name=None, degree=None):
		return ' '

	def spacing(self, full_name=None, degree=None):
		return ' '

	def guide(self):
		return f' String{self.spacing()}|     3   5   7   9     12    15  17  19  21    24'		
	

class CleanArpRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '●'
			# return '⦿'
			# return '◎'
		if degree in [3, 5]:
			# return '●'
			# return '⦿'
			return '◎'
		return ' '

	def not_found(self, full_name=None, degree=None):
		return ' '

	def spacing(self, full_name=None, degree=None):
		return ' '

	def guide(self):
		return f' String{self.spacing()}|     3   5   7   9     12    15  17  19  21    24'		

class ScaleDegreeDebugRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return 'R'
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return ' '

	def spacing(self, full_name=None, degree=None):
		return ' '

	def guide(self):
		return f' String{self.spacing()}|     3   5   7   9     12    15  17  19  21    24'		

class DegreeEmojiRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '●'
		elif degree == 3:
			return '⦿'
		elif degree == 5:
			return '◉'
		else:
			return '◎'

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'


class ColorDegreeEmojiRepresentation(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '●'
		elif degree == 3:
			return '3'
		elif degree == 5:
			return '5'
		else:
			return '⦿'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'

class DotsDegreeRepresentationWide(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '⎯⎯●'
		else:
			return '⎯⎯⦿'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		
	

class DotsDegreeRepresentationCompact(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '⎯●'
		else:
			return '⎯⦿'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String           3     5     7     9       12       15    17    19    21       24'		
	

class DotsDegreeRepresentationMicro(RepresentationInterface):
	def found(self, full_name, degree=None):
		if degree == 1:
			return '●'
		else:
			return '⦿'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String       3   5   7   9     12    15  17  19  21    24'		
	



GUITAR_REPRESENTATIONS = {
	"Dots No Strings Wide":	DotsNoStringsRepresentationWide,
	"No Strings Wide":		ScaleDegreeNoStringsRepresentationWide,
	"Basic No String Wide":	BasicNoStringsRepresentationWide,
	"Dots Wide":			DotsDegreeRepresentationWide,
	"Basic Wide":			BasicNameRepresentationWide,
	"Degree Wide":			ScaleDegreeRepresentationWide,
	"Full Name Wide":		FullNameRepresentationV2,
	"Dots Compact":			DotsDegreeRepresentationCompact,
	"Basic Compact":		BasicNameRepresentation,
	"Dots Micro":			DotsDegreeRepresentationMicro,
	"Degree":				ScaleDegreeRepresentation,
	"Degree Alt":			ScaleDegreeAltRepresentation,
	"degree_debug":			ScaleDegreeDebugRepresentation,
	"clean":				CleanRepresentation,
	"clean arp":			CleanArpRepresentation,
	# "nameless":				NamelessRepresentation,
	# "full_name":			FullNameRepresentation,
	# "note_object":			NoteRepresentation,
	# "emoji":				EmojiRepresentation,
	# "degree_emoji":		DegreeEmojiRepresentation,
	# "color_degree_emoji":	ColorDegreeEmojiRepresentation,
}
def GuitarRepresentationFactory(representation_type):
	return GUITAR_REPRESENTATIONS[representation_type]()

class Guitar:
	
	STANDARD = 'Standard'
	DROP_D = 'Drop D'
	A_SPECIAL = 'A\'s Special' 
	FIFTHS = 'Fifths' 
	BOUZOUKI = 'Bouzouki'
	SEVEN_STR = '7 String'
	TUNING_DEFINITIONS = {
		STANDARD 	: ['E3', 'A4', 'D4', 'G4', 'B5', 'E5'],
		DROP_D   	: ['D3', 'A4', 'D4', 'G4', 'B5', 'E5'],
		A_SPECIAL  	: ['C3', 'G4', 'D4', 'G4', 'B5', 'E5'],
		SEVEN_STR   : ['B3', 'E3', 'A4', 'D4', 'G4', 'B5', 'E5'],
		FIFTHS  	: ['C3', 'G4', 'D4', 'A4', 'E5', 'B6'],
		BOUZOUKI   	: ['D3', 'A4', 'E4', 'B4'],
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
			representation_type='degree_debug',
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
					degree = scale.note_names.index(fret_note.name) + 1
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

	def print_readable_basic(
			self, 
			max_fret=None, 
			return_string=True, 
			lines_to_list=False, 
			representation_type='degree_debug', 
			representation=None,
			top_guide=True,
	):
		readable_max_fret = max_fret if max_fret is None else self._max_fret
		if representation is None:
			representation = GuitarRepresentationFactory(representation_type)
		scaled_filtered_fretboard = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=self._string_tunings,
			scale=self._scale, 
			max_fret=self._max_fret,
			representation_type=representation_type,
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
	
		if not lines_to_list:
			readable = '\n'.join(readable)

		if return_string:
			return readable
		else:
			print(readable)

	