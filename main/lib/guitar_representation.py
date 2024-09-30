
import math

from typing import List
from lib.note import Note, NoteInterval
from lib.scale import Scale


class AdjustableRepresentation:
	C_SET = '◘●◉⦿◎✪⎔▸▶︎►▼◼︎🁢'
	width =3

	# Use this for now.  Figure out function later...
	DOT_OFFSET_MAP = [
			(0, 1), 
			(1, 1),
			(2, 3), # good
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
		except ValueError:
			self.dot_offset = math.ceil(width / 2) + 1
			assert False  # test later

	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		assert False, 'found() method should be overridden'

	def not_found(self, full_name=None, degree=None):
		assert False, 'not_found() method should be overridden'

	def spacing(self, full_name=None, degree=None):
		assert False, 'spacing() method should be overridden'

	# WORKING
	def guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		guide_line = f' String' + ''.ljust(self.width, ' ') + '||'
		for x in range(1, 25):
			if x in marked_frets:
				mark = x
			else:
				mark = ' '
				# mark = x
			guide_line = guide_line + f'{mark}'.ljust(2, ' ').rjust(self.width+1, ' ')
		return guide_line

	def dot_guide(self):
		marked_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
		double_marked_frets = [12, 24]
		guide_line = f'      ' + ' '.ljust(self.width+1, ' ') + '||'
		for x in range(1, 25):
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


class FullNameRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return f'●{full_name}'.rjust(3, '⎯')
		return f'{full_name}'.rjust(3, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	
	def guide(self):
		return f' String  ||            3       5       7       9          12          15      17      19      21          24'		


class FullNameRepresentationWide(AdjustableRepresentation):
	width = 6
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return f'●⎯{full_name}'.rjust(5, '⎯').ljust(6, '⎯')
		return f'{full_name}'.rjust(5, '⎯').ljust(6, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'
	

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
	
class NoStringNameRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		return Note.full_name_to_name(full_name=full_name).rjust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '  '

	def spacing(self, full_name=None, degree=None):
		return '|'

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
		return f' String   ||          3       5       7       9          12          15      17      19      21          24'		
	

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
		if degree == 1:
			return '●'	
		return f'{degree}'

	def not_found(self, full_name=None, degree=None):
		return ' '

	def spacing(self, full_name=None, degree=None):
		return '|'
	def guide(self):
		return f'String        3   5   7   9    12    15  17  19  21    24'


class ScaleDegreeRepresentationStandard(AdjustableRepresentation):
	width = 3
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


class ScaleDegreeRepresentationCompact(AdjustableRepresentation):
	width = 2
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			d = '●'
		else:
			d = degree

		return f'{d}'.rjust(2, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'


class ScaleDegreeRepresentationWide(AdjustableRepresentation):
	width = 4
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			d = '●'
		else:
			d = degree

		return f'{d}'.rjust(3, '⎯').ljust(4, '⎯')

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'


class ScaleDegreeNoStringsRepresentationWide(AdjustableRepresentation):
	width = 3
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


class ScaleDegreeNoStringsExtension1RepresentationWide(AdjustableRepresentation):
	width = 3
	def found(self, full_name, degree=None, relative_single_octave=None,
			degree_extension=None, degree_extension_octave_up=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			d = '●'
		else:
			d = degree_extension
		return ' ' + f'{d}'.ljust(2, ' ')
	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'


class ScaleDegreeNoStringsExtension2RepresentationWide(AdjustableRepresentation):
	width = 3
	def found(self, full_name, degree=None,
		degree_extension=None, degree_extension_octave_up=None,
		*args, **kwargs):
		if degree == 1:
			d = '●'
		else:
			d = degree_extension_octave_up

		return ' ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'


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
			return ' ●' + f'{name}'.ljust(2, ' ')
		else:
			return '  ' + f'{name}'.ljust(2, ' ')
		return '  ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '    '

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self):
		return f' String                   3         5         7         9             12             15        17        19        21             24'		


class BasicNoStringsRepresentationWide(AdjustableRepresentation):
	width = 3
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		
		name = Note.full_name_to_name(full_name=full_name)
		if degree == 1:
			return '●' + f'{name}'.ljust(2, ' ')
		else:
			return ' ' + f'{name}'.ljust(2, ' ')
		return ' ' + f'{d}'.ljust(2, ' ')

	def not_found(self, full_name=None, degree=None):
		return '   '

	def spacing(self, full_name=None, degree=None):
		return '|'


class CleanRepresentation(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '●'
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


class ScaleDegreeMinimalistRepresentation(RepresentationBase):
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

class DotsDegreeRepresentationWide(AdjustableRepresentation):
	width = 3
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '⎯⎯●'
		else:
			return '⎯⎯◉'			

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
	

class ExtensionRepresentation(AdjustableRepresentation):
	width = 4

	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, *args, **kwargs):
		if degree == 1:
			mark = '●'
		else:
			mark = str(degree_extension)
		mark = mark.rjust(3, '⎯').ljust(4, '⎯') 
		return mark
	
	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ExtensionRepresentationOctaveUp(AdjustableRepresentation):
	width = 4

	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, 
			degree_extension_octave_up=None, *args, **kwargs):
		if degree == 1:
			mark = '●'
		else:
			mark = str(degree_extension_octave_up)
		mark = mark.rjust(3, '⎯').ljust(4, '⎯') 
		return mark

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ThirdsExtensionRepresentation(AdjustableRepresentation):
	width = 4
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, 
			degree_extension_octave_up=None, *args, **kwargs):
		if degree == 1 and degree_extension == 1:
			mark = 'R'
		elif degree == 1 and degree_extension != 1:
			mark = self.C_SET[7]
		elif degree_extension % 2 == 0:
			mark = self.C_SET[3]
		else:
			mark = str(degree_extension)
		mark = mark.rjust(3, '⎯').ljust(4, '⎯') 
		return mark
		
	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ThirdsExtensionOctaveUpRepresentation(AdjustableRepresentation):
	width = 4
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, 
			degree_extension_octave_up=None, *args, **kwargs):
		if degree == 1 and degree_extension_octave_up == 1:
			mark = 'R'
		elif degree == 1 and degree_extension_octave_up != 1:
			mark = self.C_SET[7]
		elif degree_extension_octave_up % 2 == 0:
			mark = self.C_SET[3]
		else:
			mark = str(degree_extension_octave_up)
		mark = mark.rjust(3, '⎯').ljust(4, '⎯') 
		return mark
		
	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

class ExtensionRepresentationBothCompact(AdjustableRepresentation):
	width = 5

	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, 
			degree_extension_octave_up=None, *args, **kwargs):
		line = ''
		if degree == 1:
			return '⎯⎯R⎯⎯'
		else:
			mark = str(degree_extension)

		line = str(degree_extension).ljust(2, '⎯') + '⎯' + str(degree_extension_octave_up).rjust(2, '⎯')
		return line

	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'


class ExtensionRepresentationBothWide(AdjustableRepresentation):
	width = 7

	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, 
			degree_extension_octave_up=None, *args, **kwargs):

		mark = '⎯' + str(degree_extension).ljust(2, '⎯')
		if degree == 1:
			mark = mark + '●'
		else:
			mark = mark + '⎯'

		mark = mark + (str(degree_extension_octave_up).rjust(2, '⎯')) + '⎯'
		return mark
	def not_found(self, full_name=None, degree=None):
		return '⎯⎯⎯⎯⎯⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'


class ExtensionRepresentationCompact(AdjustableRepresentation):
	width = 2
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, degree_extension=None, *args, **kwargs):
		mark = ''
		if degree == 1:
			mark = mark + '●'
		mark = mark + str(degree_extension)
		return f'{mark}'.rjust(2, '⎯').ljust(2, '⎯')
		
	def not_found(self, full_name=None, degree=None):
		return '⎯⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'


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
	

class ArpDotsDegreeRepresentationMicro(RepresentationBase):
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


class Arp7DotsDegreeRepresentationMicro(RepresentationBase):
	def found(self, full_name, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree == 1:
			return '●'
		elif degree in [3, 5, 7]:
			return '◉'		
		else:
			return '⦿'			

	def not_found(self, full_name=None, degree=None):
		return '⎯'

	def spacing(self, full_name=None, degree=None):
		return '┼'

	def guide(self):
		return f' String       3   5   7   9     12    15  17  19  21    24'		

class DegreeExtensionRepresentationWide(AdjustableRepresentation):
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
				c = self.C_SET[8]			
			else:
				c = self.C_SET[2]

		return f'{c}'.ljust(2, '⎯').rjust(self.width, '⎯')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, '⎯')

	def spacing(self, full_name=None, degree=None):
		return '┼'

 
class DotExtensionRepresentationWide(AdjustableRepresentation):
	width = 3

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[8]		
			else:
				c = self.C_SET[2]

		return f'{c}'.ljust(2, ' ').rjust(self.width, ' ')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self, *args, **kwargs):
		return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '


class DotThrid1ExtensionRepresentationWide(AdjustableRepresentation):
	width = 3

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[11]		
			else:
				c = self.C_SET[3]

		return f'{c}'.ljust(2, ' ').rjust(self.width, ' ')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self, *args, **kwargs):
		return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '


class DotThrid2ExtensionRepresentationWide(AdjustableRepresentation):
	width = 3

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 0:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[11]		
			else:
				c = self.C_SET[3]

		return f'{c}'.ljust(2, ' ').rjust(self.width, ' ')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self, *args, **kwargs):
		return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '

class NoSDotThrid1RepresentationWide(AdjustableRepresentation):
	width = 3

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			c = ' '
			# if degree == 1:
			# 	c = self.C_SET[11]		
			# else:
			# 	c = self.C_SET[3]

		return f'{c}'.ljust(2, ' ').rjust(self.width, ' ')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self, *args, **kwargs):
		return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '

class NoSDotThrid2RepresentationWide(AdjustableRepresentation):
	width = 3

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 0:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			c = ' '
			# if degree == 1:
			# 	c = self.C_SET[11]		
			# else:
			# 	c = self.C_SET[3]

		return f'{c}'.ljust(2, ' ').rjust(self.width, ' ')
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return '|'

	def guide(self, *args, **kwargs):
		return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '

class NoSDotThrid1RepresentationMicro(AdjustableRepresentation):
	width = 1

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			# c = ' '
			if degree == 1:
				c = self.C_SET[11]		
			else:
				c = self.C_SET[3]

		return f'{c}'
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return ' '

	# def guide(self, *args, **kwargs):
	# 	return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '

class NoSDotThrid2RepresentationMicro(AdjustableRepresentation):
	width = 1

	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 0:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			# c = ' '
			if degree == 1:
				c = self.C_SET[11]		
			else:
				c = self.C_SET[3]

		return f'{c}'
	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, ' ')

	def spacing(self, full_name=None, degree=None):
		return ' '

	# def guide(self, *args, **kwargs):
	# 	return f' String   ||         3       5       7       9           12          15      17      19      21          24                              '

class ThirdDotsRepresentationCompact(AdjustableRepresentation):
	width = 3
	def found(self, full_name, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[8]			
			else:
				c = self.C_SET[3]
		return f'{c}'.ljust(2, '⎯').rjust(self.width, '⎯')

	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, '⎯')

	def spacing(self, full_name=None, degree=None):
		return '┼'


class ThirdDotsRepresentationCompactOctaveUp(AdjustableRepresentation):
	width = 3
	def found(self, full_name, degree_extension_octave_up=None, degree_extension=None, degree=None, relative_single_octave=None,
			relative_double_octave=None, *args, **kwargs):
		if degree_extension_octave_up % 2 == 1:
			if degree == 1:
				c = self.C_SET[0]
			else:
				c = self.C_SET[1]
		else:
			if degree == 1:
				c = self.C_SET[8]			
			else:
				c = self.C_SET[3]
		return f'{c}'.ljust(2, '⎯').rjust(self.width, '⎯')

	def not_found(self, full_name=None, degree=None):
		return ''.ljust(self.width, '⎯')

	def spacing(self, full_name=None, degree=None):
		return '┼'


SORTED_GUITAR_REPRESENTATIONS = {
	'Basic': {
		"Basic":				BasicNameRepresentationWide,
		"No String":			BasicNoStringsRepresentationWide,
		"Basic Compact":		BasicNameRepresentation,
		"No String Compact":	NoStringNameRepresentation,
	},
	'Dots': {
		"Dots Wide":			DotsDegreeRepresentationWide,
		"No String":			DotsNoStringsRepresentationWide,
		"Dots Compact":			DotsDegreeRepresentationCompact,
		"Arp Micro":			ArpDotsDegreeRepresentationMicro,
		"Arp7 Micro":			Arp7DotsDegreeRepresentationMicro,
		"Minimalist":			CleanRepresentation,

	},
	'Degree': {
		"Standard":				ScaleDegreeRepresentationStandard,
		"No String" :			ScaleDegreeNoStringsRepresentationWide,
		"Compact":				ScaleDegreeRepresentationCompact,
		"Wide":					ScaleDegreeRepresentationWide,
		"Extension 1":			ExtensionRepresentation,
		"Extension 2":			ExtensionRepresentationOctaveUp,
		"Extension Compact":	ExtensionRepresentationCompact,
		"No String Ext 1" :		ScaleDegreeNoStringsExtension1RepresentationWide,
		"No String Ext 2" :		ScaleDegreeNoStringsExtension2RepresentationWide,
		"Ext Both Compact":		ExtensionRepresentationBothCompact,
		"Ext Both Wide":		ExtensionRepresentationBothWide,
		"Degree Micro":			ScaleDegreeRepresentation,
		"Minimalist":			ScaleDegreeMinimalistRepresentation,
	},
	'Thirds': {
		"NoS Ext Dots":			DotExtensionRepresentationWide,
		"NoS Dots 1":			NoSDotThrid1RepresentationWide,
		"NoS Dots 2":			NoSDotThrid2RepresentationWide,
		"NoS Ext Dots 1":		DotThrid1ExtensionRepresentationWide,
		"NoS Ext Dots 2":		DotThrid2ExtensionRepresentationWide,
		"Extension 1":			ThirdsExtensionRepresentation,
		"Extension 2":			ThirdsExtensionOctaveUpRepresentation,
		"Dots Thirds Wide":		DotsThirdsRepresentationWide,
		"Ext Dots":				DegreeExtensionRepresentationWide,
		"NoS Ext Dots":			DotExtensionRepresentationWide,
		"Ext Dot Comp 1":		ThirdDotsRepresentationCompact,
		"Ext Dot Comp 2":		ThirdDotsRepresentationCompactOctaveUp,
		"Arp Micro":			ArpDotsDegreeRepresentationMicro,
		"Arp7 Micro":			Arp7DotsDegreeRepresentationMicro,
	},
	'No Strings': {
		"Dots":					DotsNoStringsRepresentationWide,
		"Degree" :				ScaleDegreeNoStringsRepresentationWide,
		"Letter Wide":			BasicNoStringsRepresentationWide,
		"Letter Ultra Wide":	BasicNoStringsRepresentationUltraWide,
		"NoS Ext Dots":			DotExtensionRepresentationWide,
		"NoS Ext Dots 1":		DotThrid1ExtensionRepresentationWide,
		"NoS Ext Dots 2":		DotThrid2ExtensionRepresentationWide,
		"NoS Dots 1":			NoSDotThrid1RepresentationWide,
		"NoS Dots 2":			NoSDotThrid2RepresentationWide,
		"NoS Dots M 1":			NoSDotThrid1RepresentationMicro,
		"NoS Dots M 2 ":		NoSDotThrid2RepresentationMicro,


	},
	'Full Name': {
		"Full Name Wide":		FullNameRepresentationWide,
		"Full Name":			FullNameRepresentation,
	},
	'Clean': {
		"clean":				CleanRepresentation,
		"clean arp":			CleanArpRepresentation,
		"NoS Dots M 1":			NoSDotThrid1RepresentationMicro,
		"NoS Dots M 2 ":		NoSDotThrid2RepresentationMicro,
	},	
}


class SortedGuitarRepresentationFactory:

	# TODO: Make this singleton ??
	# def __init__(self):
	# 	# This object will cache filtering options for style and sub_style

	@staticmethod
	def get_representation(style: str, sub_style: str):
		return SORTED_GUITAR_REPRESENTATIONS[style][sub_style]()

	@staticmethod
	def styles():
		return list(SORTED_GUITAR_REPRESENTATIONS.keys())

	@staticmethod
	def sub_styles_for_style(style):
		return list(SORTED_GUITAR_REPRESENTATIONS[style].keys())

	# @staticmethod
	# def all_substyles():
	# 	pass
