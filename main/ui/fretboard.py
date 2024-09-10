

# import math

# Example file showing a circle moving on screen
import pygame

from lib.note import Note, NoteInterval, NoteError
from ui.midi_check import print_device_info, input_main


# pygame setup
pygame.init()

# Fonts
pygame.font.init()
my_font = pygame.font.SysFont('Futura', 300)
my_font_small = pygame.font.SysFont('Futura', 40)
device_id = None
print_device_info()
# input_main()
# exit()

# if not pygame.midi.get_init():
#     pygame.midi.init()





screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


note_name = 'A'
note_octave = 4
note_sharp = False
note = Note(name=note_name, octave=note_octave)

keys_last = pygame.key.get_pressed()






# MIDI Setup
pygame.fastevent.init()
event_get = pygame.fastevent.get
event_post = pygame.fastevent.post

pygame.midi.init()

# _print_device_info()

if device_id is None:
    input_id = pygame.midi.get_default_input_id()
else:
    input_id = device_id

print("using input_id :%s:" % input_id)
i = pygame.midi.Input(input_id)

# pygame.display.set_mode((1, 1))





while running:


    if i.poll():
        midi_events = i.read(10)
        # convert them into pygame events.
        midi_evs = pygame.midi.midis2events(midi_events, i.device_id)
        print('----------')
        print(midi_events)
        print(midi_evs)
        for m_e in midi_evs:
            event_post(m_e)


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type in [pygame.midi.MIDIIN]:
            print('printing e')
            print(e)
            if e.status == 156:
                # Keydown
                note = Note(absolute_value=e.data1)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")





    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        note_name = 'A'
    elif keys[pygame.K_b]:
        note_name = 'B'
    elif keys[pygame.K_c]:
        note_name = 'C'
    elif keys[pygame.K_d]:
        note_name = 'D'
    elif keys[pygame.K_e]:
        note_name = 'E'
    elif keys[pygame.K_f]:
        note_name = 'F'
    elif keys[pygame.K_g]:
        note_name = 'G'

    if keys[pygame.K_1]:
        note_octave = 1
    elif keys[pygame.K_2]:
        note_octave = 2
    elif keys[pygame.K_3]:
        note_octave = 3
    elif keys[pygame.K_4]:
        note_octave = 4
    elif keys[pygame.K_5]:
        note_octave = 5
    elif keys[pygame.K_6]:
        note_octave = 6
    elif keys[pygame.K_7]:
        note_octave = 7
    elif keys[pygame.K_8]:
        note_octave = 8
    elif keys[pygame.K_9]:
        note_octave = 9
    elif keys[pygame.K_0]:
        note_octave = 0

    if keys[pygame.K_s] and not keys_last[pygame.K_s]:
        note_sharp = not note_sharp

    # Update Note object
    if (
            note.name[0] != note_name or 
            note.octave != note_octave or 
            note.sharp != note_sharp
        ):
        info = f"""
            {note.name} != {note_name} or 
            {note.octave} != {note_octave} or 
            {note.sharp} != {note_sharp}
        """
        print(info)
        sharp_name_part = '#' if note_sharp else ''
        # print(f'{note_name}{sharp_name_part}')
        
        #note = Note(name=f'{note_name}{sharp_name_part}', octave=note_octave) #################################


    note_name_surface = my_font.render(f'{note.full_name}', True, (0, 0, 0))
    screen.blit(note_name_surface, (40,40))


    info_text_x = 40
    info_text_y = 440
    info_text_spacing = 50
    info_text = f"Frequency: {round(note.frequency, 2)} Hz"
    note_info_surface = my_font_small.render(f'{info_text}', True, (0, 0, 0))
    screen.blit(note_info_surface, (info_text_x, info_text_y))

    info_text = f"Wavelength: {round(note.period_in_meters, 2)} m"
    note_info_surface = my_font_small.render(f'{info_text}', True, (0, 0, 0))
    screen.blit(note_info_surface, (info_text_x, info_text_y + 1 * info_text_spacing))


    # text_surface = my_font.render('Some Text', True, (0, 0, 0))
    # screen.blit(text_surface, (40,40))

    # pygame.draw.circle(screen, "red", player_pos, 40)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    keys_last = keys

pygame.quit()


# Midi cleanup
del i
pygame.midi.quit()




