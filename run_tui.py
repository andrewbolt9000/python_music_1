#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
python3 tui/fretboard_ui.py
popd