#!/usr/bin/env bash
set -eo pipefail

ENVNAME=$(basename `pwd`)
MY_PATH=`pwd`
echo Consuming from Twitter...

source activate $ENVNAME
python $MY_PATH/src/xinga_muito/build.py
