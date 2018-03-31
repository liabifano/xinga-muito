#!/usr/bin/env bash
set -eo pipefail

ENVNAME=xinga-muito
MY_PATH=$(dirname `realpath $0`)
echo Consuming from Twitter...

source activate $ENVNAME
python $MY_PATH/src/xinga_muito/main.py
