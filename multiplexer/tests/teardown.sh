#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))
BLIFFILE=$1

f="$(basename -- $BLIFFILE)"

if [ $f = "mux2i10b.blif" ] ; then

    rm $SCRIPTDIR/test_mux2i10b_correct_output.txt
    rm $SCRIPTDIR/test_mux2i10b.script

fi


if [ $f = "mux8i8b.blif" ] ; then

    rm $SCRIPTDIR/test_mux8i8b_correct_output.txt
    rm $SCRIPTDIR/test_mux8i8b.script

fi

if [ $f = "mux2i16b.blif" ] ; then

    rm $SCRIPTDIR/test_mux2i16b_correct_output.txt
    rm $SCRIPTDIR/test_mux2i16b.script

fi