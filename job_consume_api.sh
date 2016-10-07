#!/usr/bin/env bash
set -eo pipefail

ENVNAME=$(basename `pwd`)
echo Consuming from Twitter...

source activate $ENVNAME
python ~/personal/xinga-muito/src/xinga_muito/build.py
