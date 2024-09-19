# python_music_1

This is a personal project in the **prototype stage**.  
This project is an opportinity for me to practice coding while creating a tool that is useful to me personally.  The purpose of this tool is to save time by off loading musical computations to the machine and to easily display the results; rather than handwritng every permutation on endless sheets of graph paper.

## Getting started
This project contains 2 separate projects (for now).
`./main/lib/` contains a library of object useful for music computations.
`./main/tui/` contains a hacked together text ui for exploring the capablities of the library.  
### Launching Text User Interface (Unix)
From project root, run

Set up virtual environment (Suggested)
```
python -m venv venv
source venv/bin/activate
```

Install required libraries.  Run Text UI.
```
pip install -r requirements.txt
./run_tui.py
```
![image info](readme_images/demo.gif)

**Usage Tips:**
- Use `up-arrow` and `down-arrow` keys to navegate. 
- `space-bar` to make a selection.
- Also use `Mouse` to navigate, and `space-bar` to select.


## Cool things
- `NoteInterval` has a `%` operator.  Useful for `NoteInterval(semitones=13) % 12`
- Arithetic with `Note` and `NoteInterval`


## Road Map

### Library
- `Chord` class
- Generic `Scale` filters

#### Completed
- Classes: `Note`, `NoteInterval`, `Scale`, `Guitar`


#### Future Features
- For Version 1.0
	- Note naming, (flats)
	- turn into real library which can be installed via `pip`
	- add save state to TUI
- Filter Scales. Filter Scales by Chords.
- Scale - detect scale
- Chords
	- detect chord
- Doc comments
- Extend Scale to undersand extensions.
- Fretboard render uses `Notes` and their properties, (which means `Notes` would need `self.root_note`; which raises the question whether notes exist with in a tonal context??  Maybe `Scales` shoule really be made of `NoteIntervals`??  or `ScaleNote`?  We want an extened `Note` class which knows what key+scale and therfore what names it should be using for each note.)
- Pentatonic scales (non-hardcoded)


### TUI Viewer

#### Completed
- Text UI (Basic)

#### Future Features
- scale info box
- monkey patch npyscreen to print color text output...
- More midi support (without pygame.midi)

## Future related projects
- pygame gui
- api


# Design Pattern examples (To do)
Factory
Dependency Injection


