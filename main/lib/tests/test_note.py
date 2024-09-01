

import pytest

from lib.note import Note, NoteInterval, NoteError


class TestNote:


	def test_note_full_name(self):
		testee = Note(full_name='C1')
		assert testee.name == 'C'
		assert testee.octave == 1
		assert testee.absolute_value == 12

	def test_note_full_name_sharp(self):
		testee = Note(full_name='C#5')
		assert testee.name == 'C#'
		assert testee.octave == 5
		assert testee.absolute_value == 61

	def test_note_absolute_value(self):
		n1 = Note(full_name='A#3')
		a = n1.absolute_value
		n2 = Note(absolute_value=a)
		assert n1.name == n2.name 
		assert n1.octave == n2.octave 
		assert n1.full_name == n2.full_name 
		assert n1.absolute_value == n2.absolute_value 


	def test_addition_does_not_work_for_adding_notes(self):
		# A note can be added with an interval, but not another note.
		note_1 = Note(full_name='A3')
		note_2 = Note(full_name='C3')

		with pytest.raises(NoteError) as excinfo:
			result_interval = note_2 + note_1
			assert 'Cant add these types.' in str(excinfo.value)

	def test_subtraction(self):
		note_1 = Note(full_name='A3')
		note_2 = Note(full_name='C3')

		result = note_1 - note_2
		assert type(result) is NoteInterval
		assert result.semitones == 9



	def test_subtraction_negative_results(self):
		note_1 = Note(full_name='A3')
		note_2 = Note(full_name='C3')

		with pytest.raises(AssertionError) as excinfo:
			result_interval = note_2 - note_1
			assert 'For now.........' in str(excinfo.value)



class TestNoteInterval:

	def test_note_interval_init(self):
		testee = NoteInterval(5)
		assert testee.semitones == 5
		assert testee.name == 'perfect 4'


	def test_note_interval_init_with_name_kwarg(self):
		testee = NoteInterval(name='perfect 4')
		assert testee.name == 'perfect 4'
		assert testee.semitones == 5	

	def test_invalid_init(self):
		with pytest.raises(AssertionError) as excinfo:
			testee = NoteInterval()
			assert 'NoteInterval requires semitones or name args' in str(excinfo.value)

		with pytest.raises(AssertionError) as excinfo:
			testee2 = NoteInterval(name=None, semitones=None)
			assert 'NoteInterval requires semitones or name args' in str(excinfo.value)

	def test_addition(self):
		note = Note(full_name='C1')
		interval = NoteInterval(7)
		result = note + interval 
		assert type(result) is Note
		assert result.full_name == 'G1'

	def test_subtraction(self):
		note = Note(full_name='C1')
		interval = NoteInterval(7)
		result = note - interval 
		assert type(result) is Note		
		assert result.full_name == 'F0'

	def test_stepping_over_octave(self):
		interval_1 = NoteInterval(1)

		note_1 = Note(full_name='A3')
		result_1 = note_1 + interval_1
		assert result_1.full_name == 'A#3'

		note_2 = Note(full_name='A#3')		
		result_2 = note_2 + interval_1
		assert result_2.full_name == 'B3'

		note_3 = Note(full_name='B3')	
		result_3 = note_3 + interval_1
		assert result_3.full_name == 'C4'

		note_4 = Note(full_name='C4')	
		result_4 = note_4 + interval_1
		assert result_4.full_name == 'C#4'

		note_5 = Note(full_name='C#4')	
		result_5 = note_5 + interval_1
		assert result_5.full_name == 'D4'

		# Add octave
		note_6 = Note(full_name='C4')	
		result_6 = note_6 + NoteInterval(12)
		assert result_6.full_name == 'C5'
		
		# subtract octave
		note_7 = Note(full_name='C4')	
		result_7 = note_7 - NoteInterval(12)
		assert result_7.full_name == 'C3'
		
	def test_interval_name(self):
		assert NoteInterval(12).name == 'octave'

	def test_interval_name_addition(self): 
		result = NoteInterval(name='octave') + NoteInterval(name='major 2')
		assert type(result) is NoteInterval
		assert result.name == '13'

		result_2 = NoteInterval(name='octave') + NoteInterval(name='minor 2')
		assert type(result_2) is NoteInterval
		assert result_2.name == 'b 13'

