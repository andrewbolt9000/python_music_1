
from lib.guitar import Guitar
from lib.guitar_representation import GUITAR_REPRESENTATIONS
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



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(f'{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}')
# print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
