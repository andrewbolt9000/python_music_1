# JUNK SCRIPT FOR SKETCHING AND TESTING


from lib.guitar import Guitar
from lib.guitar_representation import GUITAR_REPRESENTATIONS
from lib.scale import Scale
from lib.note import Note






import curses
from curses import wrapper
from time import sleep



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

import culour
def main(stdscr):



    # Create a string with all colors
    string = ("default "
              "{black}black{end} "
              "{red}red{end} "
              "{green}green{end} "
              "{yellow}yellow{end} "
              "{blue}blue{end} "
              "{magenta}magenta{end} "
              "{cyan}cyan{end} "
              "{white}white{end} "
              "default").format(black='\033[90m',
                              red='\033[91m',
                              green='\033[92m',
                              yellow='\033[93m',
                              blue='\033[94m',
                              magenta='\033[95m',
                              cyan='\033[96m',
                              white='\033[97m',
                              end='\033[0m')

    # Add the string to the curses window
    culour.addstr(stdscr, 20, 20, string)
    stdscr.getch()


    curses.noecho()
    curses.cbreak()
    curses.start_color()
    stdscr.keypad(True)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLUE)
    stdscr.addstr(10,10,f"{bcolors.WARNING}This text should be red{bcolors.ENDC}")
    # stdscr.addstr(10,10,"This text should be red",curses.color_pair(1))
    stdscr.refresh()
    sleep(2)
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)

# Run this file in order to test culour.
# Running this should produce a curses screen, with a string that's saying the truth
import curses


exit()


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
