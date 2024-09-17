
import math

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
# print(f'{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}')
# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)


class AdjustableRepresentation:
	width =3
	# offset = 3
	# offset = math.ceil(width / 2)
	offset = width - 3

	# Use this for now.  Figure out function later...
	DOT_OFFSET_MAP = [
			(0, 1), 
			(1, 1),
			(1, 0),
			(3, 3),
			(3, 4),
			(4, 4), # 5
			(4, 5),
			(5, 5),
			(5, 6),
			(6, 6),
			(6, 7), # 10
	]


	def __init__(self):
		try:
			self.dot_offset = self.DOT_OFFSET_MAP[self.width]
			# self.dot_offset = self.DOT_OFFSET_MAP_LR[self.width]
			# self.dot_offset = self.DOT_OFFSET_MAP_RL[self.width]
		except ValueError:
			self.dot_offset = math.ceil(width / 2) + 1
			assert False  # test later


	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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


	def dot_guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		double_marked_frets = [7, 12, 19, 24]
		guide_line = f'       ' + '#'.ljust(self.width+2, '*')
		for x in range(1, 24):

			if False or x in marked_frets:
				if x in double_marked_frets:
					mark = '..'
				else:
					mark = '.'
			else:
				mark = ' '
			if len(mark) == 1:
				guide_line = guide_line + f'{mark}'.ljust(self.dot_offset[0], ' ').rjust(self.width+1, ' ')
			else:
				guide_line = guide_line + f'{mark}'.ljust(self.dot_offset[1], ' ').rjust(self.width+1, ' ')
		return guide_line



class DegreeExtensionRepresentationWide3(AdjustableRepresentation):
	width =3
	# offset = 3
	# offset = math.ceil(width / 2)
	offset = width - 3

	# Use this for now.  Figure out function later...
	DOT_OFFSET_MAP = [
			(0, 1), 
			(1, 1),
			(1, 0),
			(3, 3),
			(3, 4),
			(4, 4), # 5
			(4, 5),
			(5, 5),
			(5, 6),
			(6, 6),
			(6, 7), # 10
	]


	def __init__(self):
		try:
			self.dot_offset = self.DOT_OFFSET_MAP[self.width]
			# self.dot_offset = self.DOT_OFFSET_MAP_LR[self.width]
			# self.dot_offset = self.DOT_OFFSET_MAP_RL[self.width]
		except ValueError:
			self.dot_offset = math.ceil(width / 2) + 1
			raise ValueError

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 0:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[7]
			else:
				c = self.C_SET[5]

		return f'{c}'.ljust(2, '⎯').rjust(self.width, '⎯')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, '⎯')

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		double_marked_frets = [7, 12, 19, 24]
		guide_line = f' String ' + '#'.ljust(self.width+1, '*')
		for x in range(1, 24):

			if False or x in marked_frets:
				if x in double_marked_frets:
					mark = '..'
				else:
					mark = '.'
			else:
				# mark = ' '
				mark = x
			guide_line = guide_line + f'{mark}'.rjust(self.offset, '-').ljust(self.width+1, '_')

		return guide_line


		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		


	# WORKING
	def guide2(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		guide_line = f' String    ||'
		for x in range(1, 24):

			if x in marked_frets:
				mark = x
			else:
				mark = ' '
				# mark = x
			guide_line = guide_line + f'{mark}'.ljust(2, ' ').rjust(self.width+1, ' ')

		return guide_line


		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		
	





class RepresentationBase:
	#        0123456789
	C_SET = '◘●◉⦿◎✪⎔▸▶︎►▼◼︎🁢'
    # color_a = 'DEFAULT' # WHITE   0
    # color_a = 'DEFAULT' # WHITE   1
    # color_b = 'CURSOR'  # CYAN    2
    # color_c = 'SAFE'    # GREEN   3
    # color_d = 'CAUTION' # YELLOW  4
    # color_e = 'DANGER'  # RED     5
    # color_string = 'DANGER'
    # color_def = 'DEFAULT'         

	# ☢︎ doesnt work for equality

	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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


	def dot_guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		double_marked_frets = [7, 12, 19, 24]
		guide_line = f'       ' + '#'.ljust(self.width+2, '*')
		for x in range(1, 24):

			if False or x in marked_frets:
				if x in double_marked_frets:
					mark = '..'
				else:
					mark = '.'
			else:
				mark = ' '
			if len(mark) == 1:
				guide_line = guide_line + f'{mark}'.ljust(self.dot_offset[0], ' ').rjust(self.width+1, ' ')
			else:
				guide_line = guide_line + f'{mark}'.ljust(self.dot_offset[1], ' ').rjust(self.width+1, ' ')
		return guide_line


class NoteRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return Note(full_name=full_name)

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	
	def guide(self):
		return f' String  ||      {bcolors.OKCYAN}3      5      7      9       12     15   17   19   21     24{bcolors.ENDC}'		


class FullNameRepresentationV2(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return full_name.rjust(3, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	
	def guide(self):
		return f' String  ||            3       5       7       9          12          15      17      19      21          24'		


class FullNameRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return full_name

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'

	def guide(self):
		return f' String  |     3    5    7    9      12     15   17   19   21     24'		


class BasicNameRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return Note.full_name_to_name(full_name=full_name).rjust(2, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String  ||       3     5     7     9       12       15    17    19    21       24'		
	


class BasicNameRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return Note.full_name_to_name(full_name=full_name).rjust(3, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String  ||           3       5       7       9          12          15      17      19      21          24'		
	


class NamelessRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return 'O'

	def not_found(self, full_name=None, degree=None):
		return '+'

	def spacing(self, full_name=None, degree=None):
		return '-'


class EmojiRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ScaleDegreeRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return '┼'

	def spacing(self, full_name=None, degree=None):
		return '⎯'
	def guide(self):
		return f'String        3   5   7   9    12    15  17  19  21    24'


class ScaleDegreeAltRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	def guide(self):
		return f'String        3   5   7   9     12    15  17  19  21    24'


class ScaleDegreeRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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



class ScaleDegreeNoStringsRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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
class DotsNoStringsRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			d = '●'
		else:
			d = '◉'

		return ' ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self):
		return f' String 0    1       3       5       7       9          12          15      17      19      21          24'		

class BasicNoStringsRepresentationUltraWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		
		name = Note.full_name_to_name(full_name=full_name)
		if degree == 1:
			return ' ◉' + f'{name}'.ljust(2, ' ')
		else:
			return '  ' + f'{name}'.ljust(2, ' ')
		# if degree == 1:
		# 	d = '●'
		# else:
		# 	d = degree

		return '  ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '    '

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self):
		return f' String                   3         5         7         9             12             15        17        19        21             24'		



class BasicNoStringsRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		
		name = Note.full_name_to_name(full_name=full_name)
		if degree == 1:
			return '◉' + f'{name}'.ljust(2, ' ')
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



class CleanRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '●'
			# return '⦿'
			# return '◎'
		# return '●'
		# return '⦿'
		return '◉'
	def not_found(self, full_name=None, degree=None):
		return ' '

	def spacing(self, full_name=None, degree=None):
		return ' '

	def guide(self):
		return f' String{self.spacing()}|     3   5   7   9     12    15  17  19  21    24'		
	

class CleanArpRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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

class ScaleDegreeDebugRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return 'R'
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return ' '

	def spacing(self, full_name=None, degree=None):
		return ' '

	def guide(self):
		return f' String{self.spacing()}|     3   5   7   9     12    15  17  19  21    24'		

class DegreeEmojiRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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




class ColorDegreeEmojiRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
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

class DotsDegreeRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '⎯⎯◉'			
		else:
			return '⎯⎯●'
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		
	

class DotsThirdsRepresentationWide(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if (1 + relative_double_octave) % 2:
			if (relative_single_octave + degree) % 2:
				if degree == 1:
					c = self.C_SET[0]
				else:
					c = self.C_SET[1]
			else:
				c = self.C_SET[2]
		else:
			if (relative_single_octave + degree) % 2:
				if degree == 1:
					c = self.C_SET[8]	
				else:			
					c = self.C_SET[2]
			else:
				c = self.C_SET[1]
		
		return f'⎯⎯{c}'
		
	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		
	

class DotsDegreeRepresentationCompact(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '⎯●'
		else:
			return '⎯◉'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String           3     5     7     9       12       15    17    19    21       24'		
	

class DotsDegreeRepresentationMicro(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '●'
		elif degree == 3:
			return '◉'
		elif degree == 5:
			return '◉'
		else:
			return '⦿'			
			# return '●'

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String       3   5   7   9     12    15  17  19  21    24'		


class DotsThirdsRepresentationMicro(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		# C_SET = '◘●◉⦿◎✪☢︎⎔▸▶︎►▼◼︎🁢'
		if (1 + relative_double_octave) % 2:
			if (relative_single_octave + degree) % 2:
				if degree == 1:
					return self.C_SET[0]
				return self.C_SET[1]
			else:
				return self.C_SET[5]
		else:
			if (relative_single_octave + degree) % 2:
				if degree == 1:
					return self.C_SET[8]				
				return self.C_SET[2]
			else:
				return self.C_SET[5]
		
	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String       3   5   7   9     12    15  17  19  21    24'		

class DotsDegreeRepresentationMicro(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return self.C_SET[degree - 1]
	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String       3   5   7   9     12    15  17  19  21    24'		


class DegreeExtensionRepresentationWide(RepresentationBase):
	width = 4

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[7]			
			else:
				c = self.C_SET[2]


		return f'{c}'.ljust(2, '⎯').rjust(self.width, '⎯')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, '⎯')

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		guide_line = f'String      || '
		for x in range(1, 24):

			if x in marked_frets:
				mark = x
			else:
				mark = '.'
				# mark = x
			guide_line = guide_line + f'{x}'.ljust(3, '-').rjust(self.width+1, '_')

		return guide_line


		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		
	
class DegreeExtensionRepresentationWide2(RepresentationBase):
	width = 4

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[7]			
			else:
				c = self.C_SET[5]


		return f'{c}'.ljust(2, '⎯').rjust(self.width, '⎯')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, '⎯')

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		guide_line = f' String    || '
		for x in range(1, 24):

			if x in marked_frets:
				mark = x
			else:
				mark = '.'
				# mark = x
			guide_line = guide_line + f'{x}'.ljust(3, '-').rjust(self.width+1, '_')

		return guide_line


		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		

SORTED_GUITAR_REPRESENTATIONS = {
	'No Strings': {
		"No Strings Wide" :		ScaleDegreeNoStringsRepresentationWide,
	},
	'Dots': {

		"Micro":			DotsDegreeRepresentationMicro,
		"Dots No Strings Wide":	DotsNoStringsRepresentationWide,
		"Dots Wide":			DotsDegreeRepresentationWide,
		"Dots Compact":			DotsDegreeRepresentationCompact,

	},
	'Dot Thirds': {
		"Extension Wide":	DegreeExtensionRepresentationWide,
		"Extension Wide2":	DegreeExtensionRepresentationWide2,
		"Dots Thirds Wide":			DotsThirdsRepresentationWide,
		"Dots Degree":	DotsDegreeRepresentationMicro,
		"Dots Third":	DotsThirdsRepresentationMicro,
	},
	'Degree': {
		"Degree Wide":			ScaleDegreeRepresentationWide,
		"Degree":				ScaleDegreeRepresentation,
		"Degree Alt":			ScaleDegreeAltRepresentation,
		"degree_debug":			ScaleDegreeDebugRepresentation,
	},
	'Basic': {
		"Basic No String Ultra Wide":	BasicNoStringsRepresentationUltraWide,
		"Basic No String Wide":	BasicNoStringsRepresentationWide,
		"Basic Wide":			BasicNameRepresentationWide,
		"Basic Compact":		BasicNameRepresentation,
	},

	'Full Name': {
		"Full Name Wide":		FullNameRepresentationV2,
	},
	'Clean': {
		"clean":				CleanRepresentation,
		"clean arp":			CleanArpRepresentation,
	},	

}




	# def __init__(self):
	# 	# This object will cache filtering options for style and sub_style

def SortedGuitarRepresentationFactory(style: str, sub_style: str):
	return SORTED_GUITAR_REPRESENTATIONS[style][sub_style]()

class SortedGuitarRepresentationHelper:
	def styles():
		return list(SORTED_GUITAR_REPRESENTATIONS.keys())

	def sub_styles_for_style(style):
		return list(SORTED_GUITAR_REPRESENTATIONS[style].keys())

	# @staticmethod
	# def all_substyles():
	# 	pass





# class SortedGuitarRepresentationFactory:

# 	# def __init__(self):
# 	# 	# This object will cache filtering options for style and sub_style

# 	@staticmethod
# 	def get_representation(style: str, sub_style: str):
# 		return SORTED_GUITAR_REPRESENTATIONS[style][sub_style]()

# 	@staticmethod
# 	def styles():
# 		return list(SORTED_GUITAR_REPRESENTATIONS.keys())

# 	@staticmethod
# 	def sub_styles_for_style(style):
# 		return list(SORTED_GUITAR_REPRESENTATIONS[style].keys())

# 	# @staticmethod
# 	# def all_substyles():
# 	# 	pass




GUITAR_REPRESENTATIONS = {
	# "Color Test":			NoteRepresentation,
	# "Extension Wide3":	DegreeExtensionRepresentationWide3,
	"Extension Wide2":	DegreeExtensionRepresentationWide2,
	"Extension Wide":	DegreeExtensionRepresentationWide,
	"Dots Third":	DotsThirdsRepresentationMicro,
	"Dots Degree":	DotsDegreeRepresentationMicro,
	"Dots No Strings Wide":	DotsNoStringsRepresentationWide,
	"Basic No String Ultra Wide":	BasicNoStringsRepresentationUltraWide,
	"No Strings Wide":		ScaleDegreeNoStringsRepresentationWide,
	"Basic No String Wide":	BasicNoStringsRepresentationWide,
	"Dots Wide":			DotsDegreeRepresentationWide,
	"Dots Thirds Wide":			DotsThirdsRepresentationWide,
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
	# "emoji":				EmojiRepresentation,
	# "degree_emoji":		DegreeEmojiRepresentation,
	# "color_degree_emoji":	ColorDegreeEmojiRepresentation,
}
def GuitarRepresentationFactory(representation_type):
	return GUITAR_REPRESENTATIONS[representation_type]()
