#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))
BLIFFILE=$1

f="$(basename -- $BLIFFILE)"

if [ $f = "mux2i10b.blif" ] ; then

    python3 $SCRIPTDIR/../../test_generator.py 21 --mux --ninputs 2 --noprintstate > $SCRIPTDIR/test_mux2i10b_correct_output.txt
    python3 $SCRIPTDIR/../../test_generator.py 21 --simulate --noprintstate > $SCRIPTDIR/test_mux2i10b.script

fi


if [ $f = "mux8i8b.blif" ] ; then

    python3 $SCRIPTDIR/../../test_generator.py 67 --mux --ninputs 8 --noprintstate --endnum 5000000 > $SCRIPTDIR/test_mux8i8b_correct_output.txt
    python3 $SCRIPTDIR/../../test_generator.py 67 --simulate --noprintstate --endnum 5000000 > $SCRIPTDIR/test_mux8i8b.script

fi