
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


class Note:
	SPEED_OF_SOUND_METER_PER_SECOND = 343

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

	def __init__(self, name=None, frequency=None, a_tuning=440, semitones_from_a=None):
		self._a_tuning = a_tuning

		if name is not None:
			self._name = name.upper()
			self._frequency = Note.name_to_frequency(
				name=self._name,
				a_tuning=self._a_tuning)
		elif frequency is not None:
			self._frequency = frequency
			self._name = Note.frequency_to_name(
				frequency=self._frequency,
				a_tuning=self._a_tuning)
		elif semitones_from_a is not None:
			self._frequency = Note.frequency_of_interval(semitones=semitones_from_a, target_frequency=a_tuning)
			




	def __repr__(self):
		return f"< Note :: name:{self.name}  freq:{self._frequency}  semitones_from_a:{self.semitones_from_a} >"

	@property
	def name(self):
		if self._name is None:
			self._name = Note.frequency_to_name(
				frequency=self._frequency,
				a_tuning=self._a_tuning
			)
		return self._name 

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
		return 1 / self._frequency * self.SPEED_OF_SOUND_METER_PER_SECOND


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
		#                     frequency = target_frequency * 2 ** (semitones / 12)
		#  frequency / target_frequency = 2 ** (semitones / 12)
		#  log_2 ( frequency / target_frequency )

		#  base ^ y = x    ==>    log x = y
		base = 2
		x = frequency / target_frequency
		semitones = 12 * math.log(x, base)
		return semitones

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
		print(semitones_from_a)
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

# note = Note(frequency=440)
# note = Note(semitones_from_a=2)




print(note)
print(note.period_in_meters)

# delay_calculator = DelayCalculator()
# delay = delay_calculator.distance_to_time(distance_meter=3)
# print(delay)

