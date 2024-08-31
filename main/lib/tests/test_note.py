

import pytest

from lib.note import Note, NoteInterval


def test_note_absolute_value():
	n1 = Note(full_name='A#3')
	a = n1.absolute_value
	n2 = Note(absolute_value=a)
	assert n1.name == n2.name 
	assert n1.octave == n2.octave 
	assert n1.full_name == n2.full_name 
	assert n1.absolute_value == n2.absolute_value 
