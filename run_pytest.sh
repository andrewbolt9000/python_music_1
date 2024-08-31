#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
pytest
popd
