

import pytest

from lib.guitar import Guitar 
from lib.scale import Scale
from lib.note import Note



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
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		testee = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation_type='full_name'
		)
		assert testee == [['E3', 'F3', 0, 'G3', 0, 'A3', 0], [0, 'B4', 'C5', 0, 'D5', 0, 'E5']]


	def test_tuning_and_scale_to_fretboard_of_basic_names(self):
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		testee = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation_type='basic_name'
		)
		assert testee == [['E', 'F', None, 'G', None, 'A', None], [None, 'B', 'C', None, 'D', None, 'E']]
		

	def test_tuning_and_scale_to_fretboard_of_nameless(self):
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		testee = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation_type='nameless'
		)
		assert testee == [['O', 'O', '+', 'O', '+', 'O', '+'], ['+', 'O', 'O', '+', 'O', '+', 'O']]
		

	def test_tuning_and_scale_to_fretboard_of_degree(self):
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		testee = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation_type='degree'
		)
		assert testee == [['0', '1', '+', '2', '+', '3', '+'], ['+', '4', '5', '+', '6', '+', '0']]


	def test_tuning_and_scale_to_fretboard_of_degree_emoji(self):
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		testee = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation_type='degree_emoji'
		)
		assert testee == [['◉', '●', '┼', '●', '┼', '◎', '┼'], ['┼', '●', '⦿', '┼', '●', '┼', '◉']]


	def test_print_readable_basic(self):
		scale = Scale(root_name='A', mode_name='aeolian')
		testee = Guitar(tuning='standard', scale=scale)
		result = testee.print_readable_basic(return_string=True)
		# assert result == '1 - (E5)  O-O---O---O---O-O---O---O-O---O---O---O-O---O--\n2 - (B5)  O-O---O---O-O---O---O---O-O---O---O-O---O---O--\n3 - (G4)  O---O---O-O---O---O-O---O---O---O-O---O---O-O--\n4 - (D4)  O---O-O---O---O---O-O---O---O-O---O---O---O-O--\n5 - (A4)  O---O-O---O---O-O---O---O---O-O---O---O-O---O--\n6 - (E3)  O-O---O---O---O-O---O---O-O---O---O---O-O---O--\n'



