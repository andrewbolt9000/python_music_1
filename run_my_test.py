#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
python3 my_test.py
popd
