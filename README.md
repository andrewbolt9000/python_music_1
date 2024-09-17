# python_music_1

This is a personal project in the **prototype stage**.  
This project is an opportinity for me to practice coding while creating a tool that is useful to me personally.  The purpose of this tool is to save time by off loading musical computations to the machine and to easily display the results; rather than handwritng every permutation on endless sheets of graph paper.

## Getting started
This project contains 2 separate projects (for now).
`./main/lib/` contains a library of object useful for music computations.
`./main/tui/` contains a hacked together text ui for exploring the capablities of the library.  
### Launching Text User Interface
From project root, run

```
pip install -r requirements.txt
./run_tui.py
```
![image info](readme_images/demo.gif)

## Cool things
- `NoteInterval` has a `%` operator.  Useful for `NoteInterval(semitones=13) % 12`
- Arithetic with `Note` and `NoteInterval`


## Road Map

### Library

#### Completed
- Classes: `Note`, `NoteInterval`, `Scale`, `Guitar`


#### Future Features
- For Version 1.0
	- Note naming, (flats)
	- turn into real library which can be installed via `pip`
	- add save state to TUI
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


# Design Pattern examples (To do)
Factory
Dependency Injection


