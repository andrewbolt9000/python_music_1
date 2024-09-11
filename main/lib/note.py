

import math

class TimeInterval:
	_seconds = None
	def __init__(self, time_interval_seconds):
		self._seconds = time_interval_seconds

	def __repr__(self):
		return f'{self.seconds} seconds OR {self.milliseconds} milliseconds'

	@property
	def seconds(self):
		return self._seconds

	@property
	def milliseconds(self):
		return self._seconds * 1000


class NoteError(Exception):
    def __init__(self, message, errors=None):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
           

class NoteIntervalError(Exception):
    def __init__(self, message, errors=None):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
           

NOTE_ITERATORE_DIRECTION_HIGHER = 'higher'
NOTE_ITERATORE_DIRECTION_LOWER = 'lower'
class NoteIterator:

	NOTE_NAMES_2 = [
		'C',
		'C#',
		'D',
		'D#',
		'E',
		'F',
		'F#',
		'G',
		'G#' 
		'A',
		'A#',
		'B',
	]

	def __init__(self, start_note, direction=NOTE_ITERATORE_DIRECTION_HIGHER):
		# if stop is None:
		#     stop, start = start, 0
		# self._range = range(start, stop, step)
		# self._iter = iter(self._range)
		assert direction in [NOTE_ITERATORE_DIRECTION_HIGHER, NOTE_ITERATORE_DIRECTION_LOWER], 'invalid direction'
		
		self._start_note = start_note # string
		self._direction = direction
		self._current_note = self._start_note
		self._index = 0 
		self._stop_note = 'C8'
		
	def __iter__(self):
		return self

	def __next__(self):
		try:

			if self._current_note == self._stop_note:
				raise StopIteration
			else:
				
				# if self._current_note[0] in ['B', 'Cb']:
				# 	# increment number
				# else:
				# 	pass
				# 	# if self._current_note:

				
				self._index = self._index + 1 
				return note
			return 
		except StopIteration:
			# self._iter = iter(self._range)
			raise

class NoteInterval:
	INTERVAL_NAMES = [
		'root',
		'minor 2',
		'major 2',
		'minor 3',
		'major 3',
		'perfect 4',
		'tritone',
		'perfect 5',
		'minor 6',
		'major 6',
		'minor 7',
		'major 7',
		'octave',
		'b 13',
		'13',
		'* minor 3',
		'* major 3',
		'15',
		'tritone (sharp 15)',
		'* perfect 5',
		'b 17',
		'17',
		'* minor 7',
		'* major 7',		
	]
	_semitones = None
	_name = None
	def __init__(self, semitones=None, name=None):
		assert semitones is not None or name is not None, 'NoteInterval requires semitones or name args'
		# xor
		assert bool(semitones is not None) != bool(name is not None), 'NoteInterval can not have both semitones and name set'

		if name is not None:
			self.name = name 

		elif semitones is not None:
			# assert semitones >= 0, 'Invalid NoteInterval'
			self._semitones = semitones

	@property
	def name(self):
		if self._name is None:
			if self._semitones < 0:
				direction = '(down)'
			else:
				direction = ''
			self._name = f'{self.INTERVAL_NAMES[self._semitones]}{direction}'
		return self._name 

	@name.setter
	def name(self, value):
		# if the name is changed, update the semitones
		self._semitones = NoteInterval.name_to_semitones(name=value)

	@staticmethod
	def name_to_semitones(name):
		assert name in NoteInterval.INTERVAL_NAMES, 'invalid interval name'
		i = NoteInterval.INTERVAL_NAMES.index(name)
		return i 

	@property
	def semitones(self):
		return self._semitones 


	# This is maybe a bad idea but different types are returned based on the input types.
	def __add__(self, obj):
		if type(obj) is Note:
			raise NoteError('Cant add these types. FOR NOW')
		elif type(obj) is NoteInterval:
			result = self.semitones + obj.semitones 
			return NoteInterval(semitones=result)
		else:
			raise NoteError('Cant add these types.')



class Note:
	SPEED_OF_SOUND_METER_PER_SECOND = 343

	NOTE_NAMES_2 = [
		'C',
		'C#',
		'D',
		'D#',
		'E',
		'F',
		'F#',
		'G',
		'G#', 
		'A',
		'A#',
		'B',
	]

	NOTE_NAMES = [
		'A',
		'A#',
		'B',
		'C',
		'D',
		'D#',
		'E',
		'F',
		'F#',
		'G',
		'G#' 
	]
	_name = _frequency = _semitones_from_a = None
	_full_name = None
	_octave = None 
	_absolute_value = None 
	ABSOLUTE_VALUE_OF_A_440 = 69
	MAX_OCTAVE = 9
	MIN_OCTAVE = 0 # For now

	def __init__(self, name=None, octave=None, full_name=None, frequency=None, a_tuning=440, semitones_from_a=None, absolute_value=None):
		self._a_tuning = a_tuning

		if name is not None:
			assert octave is not None 
			validated_name_and_octave = Note.validate_name_and_octave(name=name.upper(), octave=octave)
			self._name = validated_name_and_octave['name']
			self._octave = validated_name_and_octave['octave']

		elif full_name is not None:
			name_and_octave = Note.full_name_to_name_and_octave(full_name)
			self._name = name_and_octave['name']
			self._octave = name_and_octave['octave']
			self._full_name = full_name

		elif absolute_value is not None:
			name_and_octave = Note.absolute_value_to_note_and_octave(absolute_value=absolute_value)
			self._name = name_and_octave['name']
			self._octave = name_and_octave['octave']			

	@staticmethod
	def validate_name_and_octave(name: str, octave: int):
		new_octave = Note.validate_octave(octave)

		# Is this a sketchy way or a profound way?
		# found_name, new_octave = Note.validate_name(name=name, octave=octave).value() 
		#   - It's sketchy if the arguments returned are updated or come out wrong but still accepted when unpacking.
		validated = Note.validate_name(name=name, octave=octave)
		return dict(name=validated['name'], octave=validated['octave'])

	@staticmethod
	def validate_octave(octave: int):
		if octave < Note.MIN_OCTAVE and octave > Note.MAX_OCTAVE:
			raise NoteError(f'octave must be between {Note.MIN_OCTAVE} and {Note.MAX_OCTAVE}')
		return octave 

	@staticmethod
	def validate_name(name: str, octave: int=0):
		new_octave = octave
		try:
			# Excessive...  just check that its there and return the right name
			found_name = Note.NOTE_NAMES_2[Note.NOTE_NAMES_2.index(name)]
		except ValueError:
			if Note.NOTE_NAMES_2.index(name[0]) == len(Note.NOTE_NAMES_2) - 1:
				new_octave = octave + 1 
			try:
				if name[1] == '#':
					found_name = Note.NOTE_NAMES_2[(Note.NOTE_NAMES_2.index(name[0]) + 1) % len(Note.NOTE_NAMES_2)]
				else:
					raise NoteError(f'Invalid note name: {name}.  Invalid symbol found: {name[1:]}')
			except ValueError:
				raise NoteError(f'Invalid note name: {name}')
		return dict(name=found_name, octave=new_octave)

	@staticmethod
	def full_name_to_name(full_name: str):
		validated = Note.full_name_to_name_and_octave(full_name=full_name)
		return validated['name']

	@staticmethod
	def full_name_to_name_and_octave(full_name):
		# Parse
		if full_name[1] != '#':
			name = full_name[0:1]
			octave = int(full_name[1:])
		elif full_name[1] == '#':
			name = full_name[0:2]
			octave = int(full_name[2:])
		# Validate
		assert name in Note.NOTE_NAMES_2
		assert octave in list(range(0,8))

		# VALIDATE ELSEWHERE???
		validated_name_and_octave = Note.validate_name_and_octave(name=name.upper(), octave=octave)
		name = validated_name_and_octave['name']
		octave = validated_name_and_octave['octave']

		return dict(name=name, octave=octave)



	# This is maybe a bad idea but different types are returned based on the input types.
	def __add__(self, obj):
		if type(obj) is Note:
			raise NoteError('Cant add these types.')
		elif type(obj) is NoteInterval:
			result = self.absolute_value + obj.semitones 
			return Note(absolute_value=result)
		else:
			raise NoteError('Cant add these types.')

	# This is maybe a bad idea but different types are returned based on the input types.
	def __sub__(self, obj):
		if type(obj) is Note:
			difference = self.absolute_value - obj.absolute_value
			assert difference >= 0, 'For now.........'
			return NoteInterval(semitones=difference)
		elif type(obj) is NoteInterval:
			difference = self.absolute_value - obj.semitones
			return Note(absolute_value=difference)
		else:
			raise NoteError('Cant subtract these types.')





	def __str__(self):
		# return f"< Note :: name:{self.full_name}  abs_value:{self.absolute_value} >"
		
		return f"{self.full_name}"
		return f"< Note :: name:{self.name}  freq:{self._frequency}  semitones_from_a:{self.semitones_from_a} >"

	def __repr__(self):
		# return f"< Note :: name:{self.full_name}  abs_value:{self.absolute_value} >"
		return f"Note(full_name='{self.full_name}')"
		return f"{self.full_name}"
		return f"Note(name={self.name}, octave={self._octave})"
		return f"< Note :: name:{self.name}  octave:{self._octave} abs_value:{self.absolute_value} >"
		return f"< Note :: name:{self.name}  freq:{self._frequency}  semitones_from_a:{self.semitones_from_a} >"

	@property
	def frequency(self):
		if self._frequency is None:
			difference = self.absolute_value - Note.ABSOLUTE_VALUE_OF_A_440 
			self._frequency = Note.frequency_at_semitone_away_from_target_frequency(
				semitones=difference,
				target_frequency=self._a_tuning
			)
		return self._frequency
			 
	@staticmethod
	def frequency_at_semitone_away_from_target_frequency(semitones, target_frequency):
		frequency = target_frequency * 2 ** (semitones / 12)
		return frequency


	@property
	def absolute_value(self):
		if self._absolute_value is None:
			name_semitones = Note.NOTE_NAMES_2.index(self.name)
			octave_semitones = self.octave * 12
			self._absolute_value = name_semitones + octave_semitones
		return self._absolute_value

	@staticmethod
	def absolute_value_to_note_and_octave(absolute_value):
		octave = math.floor(absolute_value / 12)
		note_index = absolute_value % 12 
		name = Note.NOTE_NAMES_2[note_index]
		return dict(name=name, octave=octave)

	@property
	def full_name(self):
		if self._full_name is None:
			self._full_name = self._name + str(self._octave)
		return self._full_name

	@property
	def octave(self):
		return self._octave

	@property
	def name(self):
		if self._name is None:
			self._name = Note.frequency_to_name(
				frequency=self._frequency,
				a_tuning=self._a_tuning
			)
		return self._name 

	@property
	def sharp(self):
		return len(self.name) > 1 and self.name[1] == '#'

	@name.setter 
	def name(self, value):
		assert False

	@property 
	def semitones_from_a(self):
		semitones_from_a = Note.semitones_from_target_frequency(
			frequency=self._frequency,
			target_frequency=self._a_tuning
		)		
		return round(semitones_from_a, 1)

	@property
	def period_in_meters(self):
		return 1 / self.frequency * self.SPEED_OF_SOUND_METER_PER_SECOND


	"""
	https://www.reddit.com/r/musictheory/comments/j3q0i3/how_can_you_calculate_the_frequency_of_a_given/

	f = f0 * 2 ^ (n / 12)

	...where:
	f is the frequency you want
	f0 is the frequency of your reference pitch (e.g. a = 440 Hz)
	n is the number of semitones above or below the reference pitch (e.g. c' is three semitones above a, so that's n = 3)

	"""
	@staticmethod
	def semitones_from_target_frequency(frequency, target_frequency):
		#                               frequency = target_frequency * 2 ** (semitones / 12)
		#            frequency / target_frequency = 2 ** (semitones / 12)
		#  log_2 ( frequency / target_frequency ) = semitones

		#  base ^ y = x    ==>    log x = y
		base = 2
		x = frequency / target_frequency
		semitones = 12 * math.log(x, base)
		return semitones



	"""

	????????????????? what is this
	"""
	@staticmethod
	def frequency_of_interval(semitones, target_frequency):
		frequency = target_frequency * 2 ** (semitones / 12)
		return frequency


	@staticmethod
	def name_to_frequency(name, a_tuning):
		name_index = Note.NOTE_NAMES.index(name)
		a_index = 0
		semitones_from_a = name_index
		# semitones_from_a = -10

		return Note.frequency_of_interval(semitones=semitones_from_a, target_frequency=a_tuning)


	@staticmethod
	def frequency_to_name(frequency, a_tuning):
		semitones_from_a = Note.semitones_from_target_frequency(
			frequency=frequency,
			target_frequency=a_tuning
		)
		a_index = 0
		return Note.NOTE_NAMES[math.floor(( a_index + semitones_from_a ) % 12)]
		# exit()




class DelayCalculator(object):
	"""docstring for DelayCalculator"""
	SPEED_OF_SOUND_METER_PER_SECOND = 343

	def __init__(self):
		super(DelayCalculator, self).__init__()
		# self.arg = arg
		
	def distance_to_time(self, distance_meter):
		seconds = distance_meter / self.SPEED_OF_SOUND_METER_PER_SECOND
		return TimeInterval(time_interval_seconds=seconds)
