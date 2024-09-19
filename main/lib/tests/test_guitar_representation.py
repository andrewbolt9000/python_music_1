

import pytest

from lib.guitar import Guitar 
# from lib.guitar_representation import Guitar 
from lib.scale import Scale
from lib.note import Note
from lib.guitar_representation import SortedGuitarRepresentationFactory, SORTED_GUITAR_REPRESENTATIONS


class TestGuitarRepresentation:

	def test_tuning_and_scale_to_fretboard_of_degree(self):
		representation = SortedGuitarRepresentationFactory.get_representation(style='Basic', sub_style='Basic')
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A#4']
		result = Guitar.tuning_and_scale_to_fretboard(
			string_tunings=test_tuning, 
			scale=test_scale, 
			max_fret=7,
			representation=representation,
		)
		assert result == [['⎯⎯E', '⎯⎯F', '⎯⎯⎯', '⎯⎯G', '⎯⎯⎯', '⎯⎯A', '⎯⎯⎯'], ['⎯⎯⎯', '⎯⎯B', '⎯⎯C', '⎯⎯⎯', '⎯⎯D', '⎯⎯⎯', '⎯⎯E']]

	def test_all_representations(self):
		# Smoke test
		test_scale = Scale(root_name='E', mode_name='phrygian', scale_type='diatonic')
		test_tuning = ['E3', 'A4']		
		for category, sub_styles in SORTED_GUITAR_REPRESENTATIONS.items():
			for sub_style in sub_styles.keys():
				testee = SortedGuitarRepresentationFactory.get_representation(style=category, sub_style=sub_style)
				result = Guitar.tuning_and_scale_to_fretboard(
					string_tunings=test_tuning, 
					scale=test_scale, 
					max_fret=7,
					representation=testee,
				)
				assert result is not None

	def test_styles(self):
		expected = ['Basic', 'Dots', 'Degree', 'Thirds', 'No Strings', 'Full Name', 'Clean']
		result = SortedGuitarRepresentationFactory.styles()
		assert expected == result

	def test_sub_styles_for_style(self):
		expected = ['Basic', 'No String', 'Basic Compact', 'No String Compact']
		result = SortedGuitarRepresentationFactory.sub_styles_for_style(style='Basic')
		assert expected == result
