#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))
BLIFFILE=$1

f="$(basename -- $BLIFFILE)"
echo "$f"

if [ $f = "mux2i10b.blif" ] ; then

    rm $SCRIPTDIR/test_mux2i10b_correct_output.txt
    rm $SCRIPTDIR/test_mux2i10b.script

fi