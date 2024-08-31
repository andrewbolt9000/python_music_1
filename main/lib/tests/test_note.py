

import pytest

from lib.note import Note, NoteInterval


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



class TestNoteInterval:

	def test_note_interval_init(self):
		testee = NoteInterval(5)
		assert testee.semitones == 5
		assert testee.interval_name == 'perfect 4'

	def test_addition(self):
		note = Note(full_name='C1')
		interval = NoteInterval(7)
		result = note + interval 
		assert result.full_name == 'G1'

		



