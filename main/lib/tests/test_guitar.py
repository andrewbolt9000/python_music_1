

import pytest

from lib.guitar import Guitar 
from lib.scale import Scale



class TestGuitar:

	def test_guitar_init(self):
		scale = Scale(root_name='A', mode_name='aeolian')
		testee = Guitar(tuning='standard', scale=scale)
		assert testee._string_tunings == ['E3', 'A4', 'D4', 'G4', 'B5', 'E5']
		
	def test_empty_fretboard(self):
		testee = Guitar.build_empty_fretboard(['A', 'B', 'C'], max_fret=10)
		assert testee == [
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]










	def test_tuning_and_scale_to_fretboard_of_notes(self):
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A4']
		testee = Guitar.tuning_and_scale_to_fretboard_of_notes(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7
		)
		print(testee)
		assert False




