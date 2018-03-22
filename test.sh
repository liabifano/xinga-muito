#!/usr/bin/env bash

ENVNAME=$(basename `pwd`)
source activate $ENVNAME
PYTHONPATH=src/ py.test $1 -vv --color=yes tests