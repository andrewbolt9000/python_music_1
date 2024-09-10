

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
		2,
		1,
		2,
		2,
		2,
		1,
	]

	# Order here is used to generate recipe
	DIATONIC_MODE_NAMES = [
		'ionian',
		'dorian',
		'phrygian',
		'lydian',
		'mixolydian',
		'aeolian',
		'locrean',
	]

	DIATONIC_MODE_ALTERNATIVE_NAMES = [
		'major',
		None,
		None,
		None,
		None,
		'minor',
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

	DIATONIC_TYPE = 'diatonic'
	MELODIC_MINOR_TYPE = 'melodic minor'
	SCALE_TYPES = [
		DIATONIC_TYPE,
		MELODIC_MINOR_TYPE,
	]

	SCALE_DEFINITIONS = {
		DIATONIC_TYPE: {
			'mode_names': DIATONIC_MODE_NAMES,
			'relative_intervals': DIATONIC_RECIPE_IONIAN,
			'alternate_names': DIATONIC_MODE_ALTERNATIVE_NAMES,
		},
		MELODIC_MINOR_TYPE: {
			'mode_names': MELODIC_MINOR_MODE_NAMES,
			'relative_intervals': MELODIC_MINOR_RECIPE_AEOLIAN,
			'alternate_names': MELODIC_MINOR_MODE_ALTERNATIVE_NAMES,
		}		
	}


	_interval_recipe = None
	_note_names = None
	_alternate_name = None
	def __init__(
			self, 
			root_name, 
			mode_name,
			scale_type=DIATONIC_TYPE,
		):
		print(Scale.SCALE_DEFINITIONS)
		validated_name = Note.validate_name_and_octave(root_name, 0)
		self.root_name = validated_name['name']

		assert scale_type in Scale.SCALE_TYPES
		self.scale_type = scale_type

		assert mode_name.lower() in Scale.SCALE_DEFINITIONS[self.scale_type]['mode_names']
		self.mode_name = mode_name.lower()

		print(self.note_names)

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
		print(f'recipe offset {recipe_offset}')

		relative_intervals = scale_definition['relative_intervals']
		interval_recipe = relative_intervals[recipe_offset:] + relative_intervals[:recipe_offset]
		print(f'interval_recipe {interval_recipe}')
		
		return interval_recipe


	# @staticmethod
	# def notes_to_scale_definition(root_note, notes):
	# 	# measure all note intervals from root
	# 	intervals = []
	# 	for note in notes:
	# 		interval = note - root_note
	# 		intervals.add(interval.semitones % 12)

	# 	# analyse intervals 
	# 	intervals = list(set(intervals))
	# 	intervals.sort()
		

	# 	return dict(root_name=root_note.name,
	# 		interval_recipe=intervals,
	# 		type=Scale.DIATONIC_TYPE,
	# 		mode=Scale.)




	# def notes_to_scale(notes):
	# 	self._root = None 


