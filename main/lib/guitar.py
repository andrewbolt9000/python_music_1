

STANDARD = 'standard'
class Guitar:
	_tuning = None 
	_max_fret = 24

	def __init__(self, tuning=STANDARD):
		self._tuning = tuning 

	def print_fretboard(self, note):
		print(note)
		
	
		