#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))
BLIFFILE=$1

f="$(basename -- $BLIFFILE)"

if [ $f = "mux2i10b.blif" ] ; then

    python3 $SCRIPTDIR/../../test_generator.py 21 --mux --ninputs 2 --noprintstate > $SCRIPTDIR/test_mux2i10b_correct_output.txt
    python3 $SCRIPTDIR/../../test_generator.py 21 --simulate --noprintstate > $SCRIPTDIR/test_mux2i10b.script

fi


if [ $f = "mux2i16b.blif" ] ; then

    python3 $SCRIPTDIR/../../test_generator.py 33 --mux --ninputs 2 --noprintstate --endnum 5000000 > $SCRIPTDIR/test_mux2i16b_correct_output.txt
    python3 $SCRIPTDIR/../../test_generator.py 33 --simulate --noprintstate --endnum 5000000 > $SCRIPTDIR/test_mux2i16b.script

fi