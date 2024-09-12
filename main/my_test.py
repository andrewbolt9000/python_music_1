
from lib.guitar import Guitar, GUITAR_REPRESENTATIONS
from lib.scale import Scale
from lib.note import Note





scale = Scale(root_name='A', mode_name='aeolian', scale_type='diatonic')

print(scale)


guitar = Guitar(
	scale=scale,
)
print(guitar)
print()
print(guitar.print_readable_basic())
print()

# print(guitar.print_readable_basic(representation_type='basic_name'))
# exit()
excluded_representation_types = [
	# 'note_object',
	# 'full_name',
	# 'basic_name',
	# 'nameless',
	# 'emoji',
	# 'degree',
	# 'degree_emoji',
	# 'color_degree_emoji',
	# 'extra_spacing',
	# 'degree_debug',
]
for representation_type in list(GUITAR_REPRESENTATIONS.keys()):
	print(f'{representation_type}')
	if representation_type not in excluded_representation_types:
		print(guitar.print_readable_basic(representation_type=representation_type))
		pass
	else:
		print('  ...skipping.')

print()



