#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# -- TEST mux4i8b

mv $SCRIPTDIR/mux4i8b_part1.blif $SCRIPTDIR/mux4i8b.blif

# -- TEST mux8i4b

mv $SCRIPTDIR/mux8i4b_part1.blif $SCRIPTDIR/mux8i4b.blif

# -- TEST mux8i8b

mv $SCRIPTDIR/mux8i8b_part1.blif $SCRIPTDIR/mux8i8b.blif

# rimuovi file extra
rm $SCRIPTDIR/mux*_part*.blif
rm $SCRIPTDIR/tests/test_mux*_part*.script
rm $SCRIPTDIR/tests/test_mux*_part*.txt