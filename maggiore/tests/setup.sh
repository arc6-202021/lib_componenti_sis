#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# copia la porta xor in questa cartella
cp $SCRIPTDIR/../../porte_logiche/xor.blif $SCRIPTDIR/..
