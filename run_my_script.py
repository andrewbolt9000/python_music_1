#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
python3 my_script.py
popd
