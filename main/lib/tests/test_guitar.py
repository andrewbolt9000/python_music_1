

import pytest

from lib.guitar import Guitar 
from lib.scale import Scale
from lib.note import Note

from lib.guitar_representation import SortedGuitarRepresentationFactory


class TestGuitar:

	def test_guitar_init(self):
		scale = Scale(root_name='A', mode_name='aeolian')
		testee = Guitar(tuning='standard', scale=scale)
		assert testee._string_tunings ==  ['E2', 'A2', 'D3', 'G3', 'B3', 'E4']
		
	def test_empty_fretboard(self):
		testee = Guitar.build_empty_fretboard(['A', 'B', 'C'], max_fret=10)
		assert testee == [
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		]

	def test_tuning_to_fretboard_of_all_notes(self):
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		result = Guitar.tuning_to_fretboard_of_all_notes(
			string_tunings=test_tuning, 
			max_fret=3
		)
		# !!! TODO: Mock Note creation
		# assert result == [
		# 	[Note(full_name='E3'), Note(full_name='F3'), Note(full_name='F#3')], 
		# 	[Note(full_name='A#4'), Note(full_name='B4'), Note(full_name='C5')]
		# ]


	def test_tuning_and_scale_to_fretboard_of_full_names(self):
		representation = SortedGuitarRepresentationFactory.get_representation(style='Basic', sub_style='Basic')
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		testee = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation=representation,
		)
		assert testee == [['⎯⎯E', '⎯⎯F', '⎯⎯⎯', '⎯⎯G', '⎯⎯⎯', '⎯⎯A', '⎯⎯⎯'], ['⎯⎯⎯', '⎯⎯B', '⎯⎯C', '⎯⎯⎯', '⎯⎯D', '⎯⎯⎯', '⎯⎯E']]

