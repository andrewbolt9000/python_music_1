# python_music_1

**This is a prototype**
This is a personal project in the prototype stage.  This library provides a objects to represent musical entities Note, NoteIntervals, Scales, Chords, Fretboards.

## Getting started
This project contains 2 separate projects (for now).
`./main/lib/` contains a library of object useful for music computations.
`./main/tui/` contains a hacked together text ui for exploring the capablities of the library.  
### Launching Text User Interface
From project root, run

`pip install -r requirements.txt`
`./run_tui.py`

## Road Map

### Library

#### Completed

#### Future Features
- turn into real library which can be installed via `pip`
- Scale - detect scale
- Chords
	- detect chord
- Doc comments

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




