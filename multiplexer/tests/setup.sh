#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))
BLIFFILE=$1

f="$(basename -- $BLIFFILE)"
echo "$f"

if [ $f = "mux2i10b.blif" ] ; then

    python3 $SCRIPTDIR/../../test_generator.py 22 --mux --ninputs 2 --noprintstate > $SCRIPTDIR/test_mux2i10b_correct_output.txt
    python3 $SCRIPTDIR/../../test_generator.py 22 --simulate --noprintstate > $SCRIPTDIR/test_mux2i10b.script

fi