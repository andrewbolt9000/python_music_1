

from lib.note import Note, NoteInterval


class ScaleError(Exception):
	def __init__(self, message, errors=None):            
		# Call the base class constructor with the parameters it needs
		super().__init__(message)
		   

class Scale(object):
	"""docstring for Scale"""

	# Other modes derived from this
	DIATONIC_RECIPE_IONIAN = [
		2,
		1,
		2,
		2,
		1,
		2,
		2,
	]

	# Order here is used to generate recipe
	DIATONIC_MODE_NAMES = [
		'aeolian',
		'locrean',
		'ionian',
		'dorian',
		'phrygian',
		'lydian',
		'mixolydian',
	]

	DIATONIC_MODE_ALTERNATIVE_NAMES = [
		'minor',
		None,
		'major',
		None,
		None,
		None,
		None,
	]

	# Other modes derived from this
	MELODIC_MINOR_RECIPE_AEOLIAN = [
		2,
		1,
		2,
		2,
		2,
		2,
		1,
	]
	# Reuse DIATONIC_MODE_NAMES but rotate list to minor mode first
	MELODIC_MINOR_MODE_NAMES = [
		'minor',
		'dorian b2',
		'lydian augmented',
		'lydian dominant', 
		'mixolydian b6',
		'aeolian b5',
		'altered',
	]
	
	MELODIC_MINOR_MODE_ALTERNATIVE_NAMES = [
		'jazz minor / melodic minor',
		'phrygian #6',
		None,
		'overtone scale',
		None,
		'locrian #2',
		'super locrian',
	]

	HARMONIC_MINOR_RECIPE_AEOLIAN = [
		2,
		1,
		2,
		2,
		1,
		3,
		1,
	]
	HARMONIC_MINOR_MODE_NAMES = [
		'harmonic minor',
		'locrian natural 6',
		'ionian #5',
		'dorian #4',
		'phrygian dominant',
		'lydian #9',
		'altered diminished',
	]
	HARMONIC_MINOR_MODE_ALTERNATIVE_NAMES = [
		None,
		None,
		None,
		None,
		None,
		None,
		'Locrian b4 bb7',
	]

	DIMINISHED_RECIPE = [
		2,
		1,
		2,
		1,
		2,
		1,
		2,
		1,
	]
	# TODO:  Make this work with capitol letters too  (lower())
	DIMINISHED_MODE_NAMES = [
		'whole-half',
		'half-whole',
	]

	WHOLE_TONE_RECIPE = [
		2,
		2,
		2,
		2,
		2,
		2,
	]
	WHOLE_TONE_MODE_NAMES = [
		'the only',
	]

	DIATONIC_TYPE = 'diatonic'
	MELODIC_MINOR_TYPE = 'melodic minor'
	DIMINISHED_TYPE = 'diminished'
	WHOLE_TONE_TYPE = 'whole tone'
	HARMONIC_MINOR_TYPE = 'harmonic minor'

	SCALE_DEFINITIONS = {
		DIATONIC_TYPE: {
			'mode_names': DIATONIC_MODE_NAMES,
			'relative_intervals': DIATONIC_RECIPE_IONIAN,
			'alternate_names': DIATONIC_MODE_ALTERNATIVE_NAMES,
		},
		HARMONIC_MINOR_TYPE: {
			'mode_names': HARMONIC_MINOR_MODE_NAMES,
			'relative_intervals': HARMONIC_MINOR_RECIPE_AEOLIAN,
			'alternate_names': HARMONIC_MINOR_MODE_ALTERNATIVE_NAMES,
		},	
		MELODIC_MINOR_TYPE: {
			'mode_names': MELODIC_MINOR_MODE_NAMES,
			'relative_intervals': MELODIC_MINOR_RECIPE_AEOLIAN,
			'alternate_names': MELODIC_MINOR_MODE_ALTERNATIVE_NAMES,
		},
		DIMINISHED_TYPE: {
			'mode_names': DIMINISHED_MODE_NAMES,
			'relative_intervals': DIMINISHED_RECIPE,
			'alternate_names': DIMINISHED_MODE_NAMES,
		},
		WHOLE_TONE_TYPE: {
			'mode_names': WHOLE_TONE_MODE_NAMES,
			'relative_intervals': WHOLE_TONE_RECIPE,
			'alternate_names': WHOLE_TONE_MODE_NAMES,
		},
	}
	SCALE_TYPES = list(SCALE_DEFINITIONS)

	_interval_recipe = None
	_note_names = None
	_alternate_name = None
	def __init__(
			self, 
			root_name, 
			mode_name,
			scale_type=DIATONIC_TYPE,
		):
		# print(Scale.SCALE_DEFINITIONS)
		validated_name = Note.validate_name_and_octave(root_name, 0)
		self.root_name = validated_name['name']

		assert scale_type in Scale.SCALE_TYPES
		self.scale_type = scale_type

		if mode_name.lower() not in Scale.SCALE_DEFINITIONS[self.scale_type]['mode_names']:
			raise ScaleError(f'invalid mode "{mode_name.lower()}" (for scale type at least.. ).  Options:{Scale.SCALE_DEFINITIONS[self.scale_type]["mode_names"]}')
		self.mode_name = mode_name.lower()

		# print(self.note_names)

	def __repr__(self):
		if self.alternate_name is not None:
			alternate_name = f' ({self.alternate_name.title()})'
		else:
			alternate_name = ''
		return f'<Scale {self.root_name} {self.mode_name.title()}{alternate_name}>'

	def __str__(self):
		if self.alternate_name is not None:
			alternate_name = f' ({self.alternate_name.title()})'
		else:
			alternate_name = ''
		note_names = ', '.join(self.note_names)
		return f'Scale: {self.root_name} {self.mode_name.title()}{alternate_name} [{note_names}]'

	@property
	def alternate_name(self):
		if self._alternate_name is None:
			name_index = Scale.SCALE_DEFINITIONS[self.scale_type]['mode_names'].index(self.mode_name)
			self._alternate_name = Scale.SCALE_DEFINITIONS[self.scale_type]['alternate_names'][name_index]
		return self._alternate_name
	
	@property
	def interval_recipe(self):
		if self._interval_recipe is None:
			self._interval_recipe = Scale.scale_name_to_interval_recipe(
				root_name=self.root_name,
				mode_name=self.mode_name,
				scale_type=self.scale_type,
			)
		return self._interval_recipe

	
	@property
	def note_names(self):
		if self._note_names is None:
			root_note = Note(name=self.root_name, octave=0)
			self._note_names = [root_note.name]
			cumulative_interval = 0
			for interval in self.interval_recipe[:-1]:
				cumulative_interval = cumulative_interval + interval
				note = root_note + NoteInterval(semitones=cumulative_interval)
				self._note_names = self._note_names + [note.name]
		return self._note_names

	@staticmethod
	def scale_name_to_interval_recipe(root_name, mode_name, scale_type):
		# Here's where some magic happens
		scale_definition = Scale.SCALE_DEFINITIONS[scale_type]
		recipe_offset = scale_definition['mode_names'].index(mode_name)
		# print(f'recipe offset {recipe_offset}')

		relative_intervals = scale_definition['relative_intervals']
		interval_recipe = relative_intervals[recipe_offset:] + relative_intervals[:recipe_offset]
		# print(f'interval_recipe {interval_recipe}')
		
		# This function is broken if it does not pass the assertion,
		# ... meaning the program is wrong not the user.
		assert sum(interval_recipe) == 12, f'Not 12.  Was {sum(interval_recipe)}'
		return interval_recipe

	@staticmethod
	def note_names_to_interval_recipe(root_name, note_names):
		root_note = Note(name=root_name, octave=0)

		# measure all note intervals from root
		intervals_relative_to_root = []
		for note_name in note_names:
			note = Note(name=note_name, octave=1)
			interval = note - root_note
			if interval.semitones % 12 != 0:
				intervals_relative_to_root.append(interval.semitones % 12)

		intervals_relative_to_root = list(set(intervals_relative_to_root))
		intervals_relative_to_root.sort()
		last_interval = 0
		interval_recipe = []
		for relative_interval in intervals_relative_to_root:
			delta = relative_interval - last_interval
			last_interval = relative_interval
			interval_recipe.append(delta)
		interval_recipe.append(12 - last_interval)
		return interval_recipe
