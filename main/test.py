from lib.guitar import Guitar
from lib.note import Note, NoteInterval

print('tested')



# note = Note(full_name='A#3')
# a = note.absolute_value
# n2 = Note(absolute_value=a)
# print(note)
# print(n2)




print('test')

note = Note(full_name='C1', a_tuning=440)
note_432 = Note(full_name='C1', a_tuning=432)
note_x = Note(full_name='C1', a_tuning=741)
print(f'start: {note}')
print(note._a_tuning)


for i in range(1, 85):
    # print('------------------')
    # print(f'i: {i}')
    if note.name == 'B':
        print('\n')
    note = note + NoteInterval(semitones=1)
    note_432 = note_432 + NoteInterval(semitones=1)
    note_x = note_x + NoteInterval(semitones=1)
    print(f'{note.full_name}  \t{note.frequency:.2f}    \t{note._a_tuning}    \t|   {note_432.full_name}  \t{note_432.frequency:.2f}    \t{note_432._a_tuning} || \t{note_x.frequency:.2f} \t{note_x._a_tuning}')


# print(note + NoteInterval(0))
# note = Note(frequency=440)
# note = Note(semitones_from_a=2)




# print(note)
# print(note.period_in_meters)

# delay_calculator = DelayCalculator()
# delay = delay_calculator.distance_to_time(distance_meter=3)
# print(delay)

