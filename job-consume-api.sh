#!/usr/bin/env bash
set -eo pipefail

#rm -rf /usr/local/var/postgres && initdb /usr/local/var/postgres -E utf8
pg_ctl -D /usr/local/var/postgres -l logfile start

ENVNAME=xinga-muito
MY_PATH=$(dirname `realpath $0`)

source deactivate
bash bootstrap-python-env.sh

echo
echo Consuming from Twitter...

source activate $ENVNAME
python $MY_PATH/src/xinga_muito/main.py
