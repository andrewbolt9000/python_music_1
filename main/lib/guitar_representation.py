
from typing import List

from lib.note import Note, NoteInterval
from lib.scale import Scale
# from lib.guitar_representation import GuitarRepresentationFactory


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
