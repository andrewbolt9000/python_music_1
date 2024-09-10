
import pytest

from lib.note import Note, NoteInterval, NoteError
from lib.scale import Scale, ScaleError


class TestNote:

	def test_basic_ionian(self):
		testee = Scale(root_name='C', mode_name='ionian', scale_type='diatonic')		
		assert testee.interval_recipe == [
			2,
			2,
			1,
			2,
			2,
			2,
			1,
		]
		assert testee.note_names == ['C', 'D', 'E', 'F', 'G', 'A', 'B']

	def test_basic_phrygian(self):
		testee = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')		
		assert testee.interval_recipe == [
			1,
			2,
			2,
			2,
			1,
			2,
			2,
		]
		assert testee.note_names == ['E', 'F', 'G', 'A', 'B', 'C', 'D']

	def test_phrygian_a(self):
		testee = Scale(root_name='A', mode_name='phrygian', scale_type='diatonic')		
		assert testee.interval_recipe == [
			1,
			2,
			2,
			2,
			1,
			2,
			2,
		]
		assert testee.note_names == ['A', 'A#', 'C', 'D', 'E', 'F', 'G']

	def test_melodic_minor_a(self):
		testee = Scale(root_name='A', mode_name='minor', scale_type='melodic minor')		
		assert testee.interval_recipe == [2, 1, 2, 2, 2, 2, 1]
		assert testee.note_names == ['A', 'B', 'C', 'D', 'E', 'F#', 'G#']

	def test_altered_scale_a(self):
		testee = Scale(root_name='A', mode_name='altered', scale_type='melodic minor')		
		assert testee.interval_recipe == [1, 2, 1, 2, 2, 2, 2]
		assert testee.note_names == ['A', 'A#', 'C', 'C#', 'D#', 'F', 'G']

	def test_str(self):
		testee = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')		
		result = str(testee)
		assert result == "Scale: E Phrygian [E, F, G, A, B, C, D]"

	def test_note_names_to_interval_recipe(self):
		result = Scale.note_names_to_interval_recipe(root_name='A', note_names=['A', 'B', 'C#', 'D', 'E', 'F#', 'G'])
		assert result == [2, 2, 1, 2, 2, 1, 2]
