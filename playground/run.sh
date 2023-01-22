#!/bin/sh

. $(dirname -- "$0")/env.sh

exec $PYTHON -m dtviz $RUN_PATH/dtviz.yaml
