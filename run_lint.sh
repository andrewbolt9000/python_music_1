#!/bin/bash

pushd main
export PYTHONPATH=$PYTHONPATH:.
flake8 --extend-ignore E203,W234,F401,E303,W391,W191,F401,W291,W292,W293
popd
