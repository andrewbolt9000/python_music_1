#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
python3 ui/fretboard.py
popd