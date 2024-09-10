#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
python3 ui/midi_check.py
popd